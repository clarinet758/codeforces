#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#start = time.clock()
n=int(raw_input())
l=map(int, raw_input().split())
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
l.sort()
if len(d)!=1:
    print l[-1]-l[0],d[l[-1]]*d[l[0]]
else:
    print 0,max(1,d[l[0]]*(d[l[0]]-1)/2)



#end = time.clock()
#print end - start
