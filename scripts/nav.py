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
	latitude = str('{:.8f}'.format(round(loc["latitude"], 8)))
	longitude = str('{:.8f}'.format(round(loc["longitude"], 8)))
	name = loc["name"]
	identifier = loc["identifier"]
	elevation = round(loc["elevation"])
	frequency = loc["frequency"]
	receptionRange = loc["receptionRange"]
	bearing = loc["bearing"]
	icao = loc["airportICAO"]
	runwayNumber = loc["associatedRunwayNumber"]
	lineType = loc["type"]
	
	lines.append(' '.join([str(lineType), latitude, longitude, str(elevation), str(frequency), str(receptionRange), str(bearing), identifier, icao, runwayNumber, name]))


## read Glideslope
with open('Glideslope.json') as data_file:
	gsData = json.load(data_file)

## iterate through each object
for gs in gsData:
	latitude = str('{:.8f}'.format(round(gs["latitude"], 8)))
	longitude = str('{:.8f}'.format(round(gs["longitude"], 8)))
	name = gs["name"]
	identifier = gs["identifier"]
	elevation = round(gs["elevation"])
	frequency = gs["frequency"]
	receptionRange = gs["receptionRange"]
	bearing = gs["bearing"]
	icao = gs["airportICAO"]
	runwayNumber = gs["associatedRunwayNumber"]
	glideslope = gs["glideslope"] * 100
	
	lines.append(' '.join(['6', latitude, longitude, str(elevation), str(frequency), str(receptionRange), str(glideslope), str(bearing), identifier, icao, runwayNumber, name]))

## save to file
with open('dat/navigation.dat', mode='wt') as currentFile:
    currentFile.write('\n'.join(lines))
