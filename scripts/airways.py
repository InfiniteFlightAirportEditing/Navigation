##
## Airways
## Converts json to dat for use in IF
##


import datetime
import sys
import json

## create array for lines
lines = []

## add headers
lines.append("I")
lines.append("810 Version - Generated using airways.py on Travis")
lines.append(" ")

## read json
with open('Airways.json') as data_file:    
    data = json.load(data_file)

## iterate through each obejct
for fix in data:
	beginningLatitude = "%.8f" % fix["beginningLatitude"]
	beginningLongitude = "%.8f" % fix["beginningLongitude"]
	beginningIntersectionName = fix["beginningIntersectionName"]

	endLatitude = "%.8f" % fix["endLatitude"]
	endLongitude = "%.8f" % fix["endLongitude"]
	endIntersectionName = fix["endIntersectionName"]

	if fix["intersectionType"] == "low":
		intersectionType = 1;
	else:
		intersectionType = 2;

	baseAltitude = int(fix["baseAltitude"]) / 100
	topAltitude = int(fix["topAltitude"]) / 100

	segmentName = fix["segmentName"]
	
	lines.append("%s %s %s %s %s %s %s %s %s %s" % (beginningIntersectionName.encode('utf-8'), beginningLatitude.encode('utf-8'), beginningLongitude.encode('utf-8'), endIntersectionName.encode('utf-8'), endLatitude.encode('utf-8'), endLongitude.encode('utf-8'), str(intersectionType).encode('utf-8'), str(baseAltitude).encode('utf-8'), str(topAltitude).encode('utf-8'), segmentName.encode('utf-8')))

## save to file
with open('dat/airways.dat', mode='wt') as currentFile:
    currentFile.write('\n'.join(lines))
