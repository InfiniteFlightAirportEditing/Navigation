import json
import sys
from collections import OrderedDict

## read json for Fixes
with open('../Fixes.json') as data_file:    
    dataF = json.load(data_file)

## iterate through each obejct and remove duplicates
seen = OrderedDict()
for d in dataF:
    oid = d["Name"]
    if oid not in seen:
        seen[oid] = d

with open('../Fixes.json', 'w') as outfile:
    json.dump(seen.values(), outfile,  indent=2)

#####

## read json for Airways
with open('../Airways.json') as data_file:    
    dataA = json.load(data_file)

## iterate through each obejct and remove duplicates
seen = OrderedDict()
for d in dataA:
    oid = d["segmentName"]
    if oid not in seen:
        seen[oid] = d

with open('../Airways.json', 'w') as outfile:
    json.dump(seen.values(), outfile,  indent=2)

#####

'''## read json for Glideslope
with open('../Glideslope.json') as data_file:    
    dataG = json.load(data_file)

## iterate through each obejct and remove duplicates
seen = OrderedDict()
for d in dataG:
    oid = d["airportICAO"]
    if oid not in seen:
        seen[oid] = d

with open('../Glideslope.json', 'w') as outfile:
    json.dump(seen.values(), outfile,  indent=2)

  '''

#####

## read json for VOR
with open('../VOR.json') as data_file:    
    dataV = json.load(data_file)

## iterate through each obejct and remove duplicates
seen = OrderedDict()
for d in dataV:
    oid = d["identifier"]
    if oid not in seen:
        seen[oid] = d

with open('../VOR.json', 'w') as outfile:
    json.dump(seen.values(), outfile,  indent=2)
