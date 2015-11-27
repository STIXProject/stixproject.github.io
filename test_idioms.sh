#!/bin/bash

: ${VERBOSE:=0}

validator=stix-validator.py

realpath() { echo $(cd $(dirname $1); pwd)/$(basename $1); }

log()
{
    (( "$VERBOSE" != 0 )) && echo -e "$1"
}

# Run with redirection of stderr according to the
# verbosity setting.
run_redir()
{
    if (( "$VERBOSE" != 0 )) ; then
        "$@"
    else
        "$@" 2> /dev/null
    fi
}

run_producer_consumer()
{
    local producer="$1"
    local stem="${producer%producer.py}"
    local consumer="${stem}consumer.py"
    local outfile="${stem}out.xml"
    local parsedfile="${stem}parsed.txt"

    /bin/rm -f "$outfile" "$parsedfile"
    
    log "  Producer: $producer"
    run_redir python "$producer" > "$outfile"
    if (( $? != 0 )) || [[ ! -e "$outfile" ]] ; then
        return 1
    fi

    if [[ -f "$consumer" ]] ; then
        log "  Consumer: $consumer"
        run_redir python "$consumer" "$outfile" > "$parsedfile"
        if (( $? != 0 )) || [[ ! -e "$parsedfile" ]] ; then
            return 2 # special status meaning consumer error
        fi
    fi

    return 0
}

# User can specify their own idiom dirs if they want.
if (( $# > 0 )) ; then
    IDIOM_DIRS="$@"
else
    IDIOM_DIRS=./documentation/idioms/*
fi

# Not every idiom dir has any *.py files.
# Let fileglobs expand to "" in that case.
shopt -s nullglob

RETVAL=0
for dir in $IDIOM_DIRS; do
    [[ -d "$dir" ]] || continue

    log "Idiom: $dir"
    pushd "$dir" > /dev/null  #change to idiom directory

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
                status=$?
                if (( $status != 0 )) ; then
                    # disambiguate whether producer or consumer failed
                    (( $status == 1 )) && ERR_FILE="$scriptfile" ||
                        ERR_FILE="${scriptfile%producer.py}consumer.py"
                    echo -e "\nERROR running $(realpath $ERR_FILE)"
                    RETVAL=1
                fi
                ;;
            *consumer.py)
                continue
                ;;
            *)
                log "  Run: $scriptfile"
                run_redir python "$scriptfile" > /dev/null
                if (( $? != 0 )) ; then
                    echo -e "\nERROR running $(realpath $scriptfile)"
                    RETVAL=1
                fi
                ;;
        esac

        # in verbose mode, the "."s would be drowned out
        # by log messages and be kinda pointless...
        [ "$VERBOSE" -eq 0 ] && echo -n "."
    done

    for xmlfile in ./*.xml ; do
        log "  Validate: $xmlfile"
        run_redir "$validator" "$xmlfile" > /dev/null
        if (( $? != 0 ))
        # the file had validation errors
        then
            echo -e "\nERROR: $(realpath $xmlfile) had validation errors"
            RETVAL=1
        else
            (( "$VERBOSE" == 0 )) && echo -n "."
        fi
    done

    popd > /dev/null #return to root dir
done

echo -e "\nDone!"
exit $RETVAL
