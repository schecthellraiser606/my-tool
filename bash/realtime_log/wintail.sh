#!/bin/bash -
#
# Cybersecurity Ops with bash
# wintail.sh
#
# Description: 
# Perform a tail-like function on a Windows log
#
# Usage: ./wintail.sh 
#

WINLOG="Application" 

LASTLOG=$(wevtutil qe "$WINLOG" //c:1 //rd:true //f:text) 

while true
do
	CURRENTLOG=$(wevtutil qe "$WINLOG" //c:1 //rd:true //f:text) 
	if [[ "$CURRENTLOG" != "$LASTLOG" ]]
	then		
		echo "$CURRENTLOG"
		echo "----------------------------------"
		LASTLOG="$CURRENTLOG"
	fi
done