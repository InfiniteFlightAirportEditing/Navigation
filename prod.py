##
## Converts json to dat for use in IF
##

import datetime
import sys

## create array for lines
lines = []

## add headers
lines.append("I")
lines.append("810 Version - Created on " + datetime.datetime.now())

## save to file
with open(sys.argv[1]) as lines, open('out.txt', 'w') as out:
    for line in lines:
       if line.strip():                     #checks if line is not empty
           out.write(line.split()[0]+'\n')
           print line
