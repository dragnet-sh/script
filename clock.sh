#!/bin/bash

LA="America/Los_Angeles"
NP="Asia/Kathmandu"

TIMEZONE="$LA $NP"
for TZ in $TIMEZONE ; do
	TIME=$( TZ=$TZ date +"%A %r" )
	echo -e $TIME "\t" $TZ
done
