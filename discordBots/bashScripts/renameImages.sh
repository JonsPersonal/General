#!/bin/bash
filename="newfy"
imageCount=10
needToChange=$(ls | grep -c .jpg)
echo "files that need to change: $needToChange"
for file in *.jpg 
do
newName="$filename $imageCount.png"
mv "${file}" "${newName}"
imageCount=$((imageCount + 1))
done
echo "$imageCount" > imagecount.txt
