#!/bin/bash
start="TU5aZFFMYUlKZmVjRk9FYktQ.7z"
# count=`ls -1 *.7z | wc -l`
while [[ $(ls -1 *.7z | wc -l) == 1 ]]; do
    pass=`ls *.7z | sed 's/\.7z//' | base64 -d`
    filename=`7z t $start -ptest | awk '{print $2}' | grep 7z | sed 's/\.7z//'`
    7z x $start -p$pass
    rm $start
    start=$filename".7z"
    echo $start
done
