#!/usr/bin/python
import sys

result=0
for line in sys.stdin:
    result+=int(line)
print result
