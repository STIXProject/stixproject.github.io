#!/bin/bash
#iterate directories to find ones with .py files
for dir in ./documentation/idioms/*; do
    if [ -d $dir ] 
    then
        pushd $dir  #change to idiom directory

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

        popd #return to root dir
    fi
done;

exit 0
