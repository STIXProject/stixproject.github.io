#!/bin/bash

: ${VERBOSE:=0}

validator=stix-validator.py

function realpath { echo $(cd $(dirname $1); pwd)/$(basename $1); }

function log
{
    [ "$VERBOSE" -ne 0 ] && echo -e "$1"
}

function run_producer_consumer
{
    local producer=$1
    local stem="${producer%producer.py}"
    local consumer="${stem}consumer.py"
    local outfile="${stem}out.xml"
    local parsedfile="${stem}parsed.txt"

    rm -f "$outfile" "$parsedfile"
    
    log "  Producer: $producer"
    python "$producer" > "$outfile" 2>/dev/null
    if [[ $? -ne 0 || ! -e "$outfile" ]] ; then
        return 1
    fi

    if [ -f "$consumer" ] ; then
	log "  Consumer: $consumer"
        python "$consumer" "$outfile" > "$parsedfile" 2>/dev/null
        if [[ $? -ne 0 || ! -e "$parsedfile" ]] ; then
            return 1
        fi
    fi

    return 0
}

# User can specify their own idiom dirs if they want.
if [ $# -gt 0 ] ; then
    IDIOM_DIRS="$@"
else
    IDIOM_DIRS=./documentation/idioms/*
fi

# Not every idiom dir has any *.py files.
# Let fileglobs expand to "" in that case.
shopt -s nullglob

RETVAL=0
for dir in $IDIOM_DIRS; do
    [ -d $dir ] || continue

    log "Idiom: $dir"
    pushd $dir > /dev/null  #change to idiom directory

    # Assume sets of paired scripts, named *producer.py and
    # *consumer.py.  The output of *producer.py is checked
    # with *consumer.py.
    #
    # Any misc scripts which don't conform to this naming
    # convention are just run and checked for exit status.
    #
    # Dangling producer scripts are simply run for exit status.
    # Dangling consumer scripts are ignored.

    for scriptfile in *.py ; do
	case "$scriptfile" in
	    *producer.py)
		run_producer_consumer "$scriptfile"
		;;
	    *consumer.py)
		true
		;;
	    *)
		log "  Run: $scriptfile"
		python "$scriptfile" > /dev/null 2>&1
		;;
        esac

	if [ $? -eq 0 ] ; then
	    # maybe in verbose mode, the "."s would be drowned out
	    # by log messages and be kinda pointless...
            [ "$VERBOSE" -eq 0 ] && echo -n "."
	else
            echo -e "\nERROR running $(realpath $scriptfile)"
	    RETVAL=1
	fi
    done

    for xmlfile in ./*.xml ; do
	log "  Validate: $xmlfile"
        python "$validator" "$xmlfile" > /dev/null 2>&1
        if [ $? -ne 0 ]
        # the file had validation errors
        then
            echo -e "\nERROR: $(realpath $xmlfile) had validation errors"
            RETVAL=1
        else
            [ "$VERBOSE" -eq 0 ] && echo -n "."
        fi
    done

    popd > /dev/null #return to root dir
done

echo -e "\nDone!"
exit $RETVAL
