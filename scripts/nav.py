##
## Navigation
## Converts json to dat for use in IF
##

import datetime
import sys
import json

NoneType = type(None)

## create array for lines
lines = []

## add headers
lines.append("I")
lines.append("810 Version - Generated using nav.py on GitHub Actions")
lines.append(" ")

## read LOC
with open('LOC.json') as data_file:
	locData = json.load(data_file)

## iterate through each object
for loc in locData:
	latitude = str("%.8f" % loc["latitude"])
	longitude = str("%.8f" % loc["longitude"])
	name = str(loc["name"])
	identifier = loc["identifier"]
	elevation = int(loc["elevation"])
	frequency = loc["frequency"]
	receptionRange = loc["receptionRange"]
	bearing = loc["bearing"]
	icao = loc["airportICAO"]
	runwayNumber = loc["associatedRunwayNumber"]
	lineType = loc["type"]
	
	lines.append(' '.join([str(lineType).encode('utf-8'), latitude.encode('utf-8'), longitude.encode('utf-8'), str(elevation).encode('utf-8'), str(frequency).encode('utf-8'), str(receptionRange).encode('utf-8'), str(bearing).encode('utf-8'), identifier.encode('utf-8'), icao.encode('utf-8'), runwayNumber.encode('utf-8'), name.encode('utf-8')]))


## read Glideslope
with open('Glideslope.json') as data_file:
	gsData = json.load(data_file)

## iterate through each object
for gs in gsData:
	latitude = str("%.8f" % gs["latitude"])
	longitude = str("%.8f" % gs["longitude"])
	name = str(gs["name"])
	identifier = gs["identifier"]
	elevation = int(gs["elevation"])
	frequency = gs["frequency"]
	receptionRange = gs["receptionRange"]
	bearing = gs["bearing"]
	icao = gs["airportICAO"]
	runwayNumber = gs["associatedRunwayNumber"]
	glideslope = int(gs["glideslope"] * 100)

	if type(identifier) is NoneType:
		identifier = ""

	if type(runwayNumber) is NoneType:
		runwayNumber = ""	

	if type(icao) is NoneType:
		icao = ""

	if type(name) is NoneType:
		name = ""
	
	lines.append(' '.join(['6', latitude.encode('utf-8'), longitude.encode('utf-8'), str(elevation).encode('utf-8'), str(frequency).encode('utf-8'), str(receptionRange).encode('utf-8'), str(glideslope).encode('utf-8'), str(bearing).encode('utf-8'), identifier.encode('utf-8'), icao.encode('utf-8'), runwayNumber.encode('utf-8'), name.encode('utf-8')]))

## save to file
with open('dat/navigation.dat', mode='wt') as currentFile:
    currentFile.write('\n'.join(lines))
