#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys, io
import re, math
#start = time.clock()
gu,ki=[],[]
ans=0
n=int(raw_input())
a=map(int, raw_input().split())
a.sort()
for i in a:
    if i%2==0:
        gu.append(i)
    else:
        ki.append(i)
if len(ki)==0:
    print ans
    sys.exit()
print sum(gu)+sum(ki) if len(ki)%2!=0 else sum(gu)+sum(ki[1:])

#end = time.clock()
#print end - start
