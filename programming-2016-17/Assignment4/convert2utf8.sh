#!/bin/bash

# author: Philip Schulz
# This script is needed to convert the 20 newsgroups data set to utf8

for DIR in $1/*
do 
	echo $DIR
	for FILE in $DIR/*
	do 
		echo $FILE
		iconv -t utf-8 $FILE > $FILE.temp
		mv $FILE.temp $DIR/`basename $FILE.temp .temp`
	done
done
