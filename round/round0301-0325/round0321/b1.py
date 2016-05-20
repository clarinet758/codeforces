#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
import collections
import bisect
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.141592653589
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
#start = time.clock()

n,d=map(int,raw_input().split())
bl={}
for i in range(n):
    m,s=map(int,raw_input().split())
    if bl.has_key(m):
        bl[m]+=s
    else:
        bl[m]=s
ls=[]
for i in bl:
    ls.append((i,bl[i]))
ls.sort()
ans=tmp=b=0
lst=len(ls)
for i in range(lst):
    tmp+=ls[i][1]
    if ls[i][0]-ls[b][0]>=d:
        while 1:
            tmp-=ls[b][1]
            b+=1
            if ls[i][0]-ls[b][0]<d:
                break
    ans=max(ans,tmp)
print ans

#end = time.clock()
#print end - start
