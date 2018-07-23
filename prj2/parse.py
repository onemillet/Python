#!/usr/bin/env python

from optparse import OptionParser
import sys

parser=OptionParser()
parser.add_option("-c","--char",
                    dest="chars",
                    action="store_true",
                    default=False,
                    help="only count chars")

parser.add_option("-w","--word",
                    dest="words",
                    action="store_true",
                    default=False,
                    help="only count words")

parser.add_option("-l","--line",
                    dest="lines",
                    action="store_true",
                    default=False,
                    help="only count lines")

options,args=parser.parse_args()
print options,args
print options.words,args

if not (options.chars or options.words or options.lines):
    options.chars,options.words,options.lines=True,True,True

data=sys.stdin.read()
chars=len(data)
words=len(data.split())
lines=data.count('\n')

if options.chars:
    print chars,
if options.words:
    print words,
if options.lines:
    print lines

