#!/usr/bin/python
import sys
finallist=[]
for line in sys.stdin:
    linelist = line.strip().split(' ')
    for x in linelist:
        finallist.append(int(x))
finallist.sort()
for x in finallist:
    print x,