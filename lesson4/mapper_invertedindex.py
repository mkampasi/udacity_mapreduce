#!/usr/bin/python
import sys
import csv
count=0

#Split forum post on the given set of delimiters
def multisplit(s, delims):
    pos = 0
    for i, c in enumerate(s):
        if c in delims:
            yield s[pos:i].upper()
            pos = i + 1
    yield s[pos:].upper()


count=0
reader = csv.reader(open("forum_node.tsv"), delimiter='\t')
for line in reader:
    if len(line)<5:
        continue
    body = line[4]
    bodylist = list(multisplit(body,' .,!?:;()<>[]#$=-/"'))
    count+=bodylist.count('FANTASTIC')
print count
