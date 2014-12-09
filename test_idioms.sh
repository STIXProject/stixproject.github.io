#!/bin/bash
#iterate directories to find ones with .py files

validator=stix_validator.py

function realpath { echo $(cd $(dirname $1); pwd)/$(basename $1); }

RETVAL=0
for dir in ./documentation/idioms/*; do
    if [ -d $dir ] 
    then
        pushd $dir > /dev/null  #change to idiom directory

        for producer in ./*producer.py ; do
        if [ -e $producer ]
        then
            `python $producer > out.xml 2>/dev/null`
            if [[ -e out.xml && $? -eq 0 ]]
            then
                echo -n "."
            else
                echo -e "\nERROR running $(realpath $producer)"
                RETVAL=1
                continue
            fi
        fi
        done

        for consumer in ./*consumer.py ; do
        if [ -e $consumer ]
        then
            `python $consumer out.xml > out.parsed 2>/dev/null`
            if [[ -e out.parsed && $? -eq 0 ]]
            then
                echo -n "."
            else
                echo -e "\nERROR running $(realpath $consumer)"
                RETVAL=1
                continue
            fi
        fi
        done

        for xmlfile in ./*xml ; do
        if [ -e $xmlfile ]
        then
            $($validator $xmlfile | grep -q INVALID)
            if [ $? -eq 0 ]
            # the file had validation errors
            then
                echo -e "\nERROR: $(realpath $xmlfile) had validation errors"
                RETVAL=1
                continue
            else
                echo -n "."
            fi
        fi
        done

        popd > /dev/null #return to root dir
    fi
done;

echo -e "\nDone!"
exit $RETVAL
