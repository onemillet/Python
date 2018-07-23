#!/usr/bin/python

import sys
import os

try:
    fn=sys.argv[1]
except IndexError:
    print "Please follow a argument at %s"%__file__
    sys.exit()
if not os.path.exists(fn):
    print "%s don't exists"%fn
    sys.exit()

fd=open(sys.argv[1])
data=fd.read()
chars=len(data)
words=len(data.split())
lines=data.count('\n')

print "%(lines)s %(words)s %(lines)s"%locals()
