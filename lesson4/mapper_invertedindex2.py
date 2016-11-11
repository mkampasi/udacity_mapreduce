#!/usr/bin/python
import sys
import csv
result=[]
def multisplit(s, delims):
    pos = 0
    for i, c in enumerate(s):
        if c in delims:
            yield s[pos:i].upper()
            pos = i + 1
    yield s[pos:].upper()

reader = csv.reader(open("forum_node.tsv"), delimiter='\t')
for line in reader:
    if len(line)<5:
        continue
    body = line[4]
    bodylist = list(multisplit(body,' .,!?:;()<>[]#$=-/"'))
    if 'FANTASTICALLY' in bodylist:
        result.append(int(line[0]))
result.sort() 
for x in result:
    print x,