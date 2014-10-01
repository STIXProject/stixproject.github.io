#!/bin/bash
#iterate directories to find ones with .py files

validator=$PWD/stix-validator/sdv.py

for dir in ./documentation/idioms/*; do
    if [ -d $dir ] 
    then
        pushd $dir > /dev/null  #change to idiom directory

        for producer in ./*producer.py ; do
        if [ -e $producer ]
        then
            echo Running $producer
            `python $producer > out.xml 2>/dev/null`
            if [[ -e out.xml && $? -eq 0 ]]
            then
                echo "."
            else
                echo "error in $producer"
                exit 1
            fi
        fi
        done

        for consumer in ./*consumer.py ; do
        if [ -e $consumer ]
        then
            echo Running $consumer
            `python $consumer out.xml > out.parsed 2>/dev/null`
            if [[ -e out.parsed && $? -eq 0 ]]
            then
                echo "."
            else
                echo "error in $consumer"
                exit 1
            fi
        fi
        done
        
        for xmlfile in ./*xml ; do
        if [ -e $xmlfile ]
        then
            echo Checking $xmlfile for well-formedness
            $($validator $xmlfile | grep INVALID)
            if [[ $? -eq 0 ]]
            # the file had validation errors
            then
                echo "validation failure for $xmlfile"
                exit 1
            else
                echo "."
            fi
        fi
        done

        popd > /dev/null #return to root dir
    fi
done;

exit 0
