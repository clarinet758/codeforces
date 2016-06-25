#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
import collections
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.141592653589
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
#start = time.clock()
n=int(raw_input())
ans=[]
hl=range(1,n+1)
vl=range(1,n+1)
for i in range(n**2):
    x,y=map(int,raw_input().split())
    if x in hl and y in vl:
        ans.append(str(i+1))
        hl.remove(x)
        vl.remove(y)
print ' '.join(ans)
#l=map(int,raw_input().split())
#ans=chk=0
#end = time.clock()
#print end - start
