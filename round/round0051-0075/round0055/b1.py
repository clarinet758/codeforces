#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys, io
import re, math
#start = time.clock()
n=input()
l=map(int,raw_input().split())
o,e=[],0
for i in l:
    if i%2:
        o.append(i)
    else:
        e+=i
o.sort()
if len(o)==0:
    print 0
elif len(o)%2:
    print e+sum(o)
else:
    o.pop(0)
    print e+sum(o)

#end = time.clock()
#print end - start
