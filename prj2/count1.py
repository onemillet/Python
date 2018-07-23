#!/usr/bin/env python

import sys

data=sys.stdin.read()
chars=len(data)
words=len(data.split())
lines=data.count('\n')

#print chars,words,lines
#print "%(lines)s %(words)s %(chars)s"%locals()
print "%(lines)s %(words)s %(chars)s"%{'lines':lines,'words':words,'chars':chars}
