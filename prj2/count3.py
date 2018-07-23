#!/usr/bin/env python

import sys
import os

if len(sys.argv)==1:
    data=sys.stdin.read()
else:
    try:
        fn=sys.argv[1]
    except IndexError:
        print "Please follow a argumenr at %s"%__file__
        sys.exit()
    if not os.path.exists(fn):
        print "%s don't exist"%fn
        sys.exit()
    fd=open(sys.argv[1])
    data=fd.read()
    fd.close()

chars=len(data)
words=len(data.split())
lines=data.count('\n')

print "%(chars)s %(words)s %(lines)s"%locals()
