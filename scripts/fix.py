##
## Fixes
## Converts json to dat for use in IF
##

import datetime
import sys

## create array for lines
lines = []

## add headers
lines.append("I")
lines.append("810 Version - Created on " + str(datetime.datetime.now()))

## save to file
with open('/fix.dat', mode='wt', encoding='utf-8') as currentFile:
    currentFile.write('\n'.join(lines))
