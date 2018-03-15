##
## Fixes
## Converts json to dat for use in IF
##

import datetime
import sys
import json

## create array for lines
lines = []

## add headers
lines.append("I")
lines.append("810 Version - Generated using fix.py on Travis")
lines.append(" ")

## read json
with open('Fixes.json') as data_file:    
    data = json.load(data_file)

## iterate through each obejct
for fix in data:
	latitude = "%.8f" % fix["Latitude"]
	longitude = "%.8f" % fix["Longitude"]
	name = fix["Name"]
	
	lines.append("%s %s %s" % (latitude.encode('utf-8'), longitude.encode('utf-8'), name.encode('utf-8')))

## save to file
with open('dat/fix.dat', mode='wt') as currentFile:
    currentFile.write('\n'.join(lines))
