import json
import sys
from collections import OrderedDict



## read json for Glideslope
with open('../LOC.json') as data_file:    
    dataG = json.load(data_file)

## iterate through each obejct and remove duplicates
seen = OrderedDict()
for d in dataG:
    oid = d["airportICAO"] + "___" + d["identifier"]
    seen[oid] = d

with open('../LOC_deduped.json', 'w') as outfile:
    json.dump(seen.values(), outfile,  indent=2)
