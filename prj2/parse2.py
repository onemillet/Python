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
if not (options.words or options.lines or options.chars):
    options.chars,options.words,options.lines=True,True,True

if args:
    fn=args[0]
    with open(fn) as fd:
        data=fd.read()
else:
    data=sys.stdin.read()
    fn=''

chars=len(data)
words=len(data.split())
lines=data.count('\n')

if options.lines:
    print lines,
if options.words:
    print words,
if options.chars:
    print chars,
    print fn
