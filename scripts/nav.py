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
lines.append("810 Version - Generated using nav.py on Travis")
lines.append(" ")

## read NDB
with open('NDB.json') as data_file:
	ndbData = json.load(data_file)

## iterate through each object
for ndb in ndbData:
	latitude = str("%.8f" % ndb["latitude"])
	longitude = str("%.8f" % ndb["longitude"])
	name = str(ndb["name"])
	identifier = ndb["identifier"]
	elevation = int(ndb["elevation"])
	frequency = ndb["frequency"]
	receptionRange = ndb["receptionRange"]
	
	lines.append("2 %s %s %s %s %s 0.0 %s %s" % (latitude.encode('utf-8'), longitude.encode('utf-8'), str(elevation).encode('utf-8'), str(frequency).encode('utf-8'), str(receptionRange).encode('utf-8'), identifier.encode('utf-8'), name.encode('utf-8')))


## read VOR
with open('VOR.json') as data_file:
	vorData = json.load(data_file)

## iterate through each object
for vor in vorData:
	latitude = str("%.8f" % vor["latitude"])
	longitude = str("%.8f" % vor["longitude"])
	name = str(vor["name"])
	identifier = vor["identifier"]
	elevation = int(vor["elevation"])
	frequency = vor["frequency"]
	receptionRange = vor["receptionRange"]
	slavedVariation = vor["slavedVariation"]
	
	lines.append("3 %s %s %s %s %s %s %s %s" % (latitude.encode('utf-8'), longitude.encode('utf-8'), str(elevation).encode('utf-8'), str(frequency).encode('utf-8'), str(receptionRange).encode('utf-8'), str(slavedVariation).encode('utf-8'), identifier.encode('utf-8'), name.encode('utf-8')))


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
	
	lines.append("%s %s %s %s %s %s %s %s %s %s %s" % (str(lineType).encode('utf-8'), latitude.encode('utf-8'), longitude.encode('utf-8'), str(elevation).encode('utf-8'), str(frequency).encode('utf-8'), str(receptionRange).encode('utf-8'), str(bearing).encode('utf-8'), identifier.encode('utf-8'), icao.encode('utf-8'), runwayNumber.encode('utf-8'), name.encode('utf-8')))


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
	
	lines.append("6 %s %s %s %s %s %s%s %s %s %s %s" % (latitude.encode('utf-8'), longitude.encode('utf-8'), str(elevation).encode('utf-8'), str(frequency).encode('utf-8'), str(receptionRange).encode('utf-8'), str(glideslope).encode('utf-8'), str(bearing).encode('utf-8'), identifier.encode('utf-8'), icao.encode('utf-8'), runwayNumber.encode('utf-8'), name.encode('utf-8')))

## read MB
with open('MarkerBeacons.json') as data_file:
	mbData = json.load(data_file)

## iterate through each object
for mb in mbData:
	latitude = str("%.8f" % mb["latitude"])
	longitude = str("%.8f" % mb["longitude"])
	name = str(mb["name"])
	elevation = int(mb["elevation"])
	bearing = mb["bearing"]
	icao = mb["airportICAO"]
	runwayNumber = mb["associatedRunwayNumber"]
	lineType = mb["type"]
	
	lines.append("%s %s %s %s 0 0 %s ---- %s %s %s" % (str(lineType).encode('utf-8'), latitude.encode('utf-8'), longitude.encode('utf-8'), str(elevation).encode('utf-8'), str(bearing).encode('utf-8'), icao.encode('utf-8'), runwayNumber.encode('utf-8'), name.encode('utf-8')))


## read DME
with open('DME.dat') as data_file:
	dmeData = json.load(data_file)

## iterate through each object
for dme in dmeData:
	lines.append(dme.encode('utf-8'))

## save to file
with open('dat/navigation.dat', mode='wt') as currentFile:
    currentFile.write('\n'.join(lines))
