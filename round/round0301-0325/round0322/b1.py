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
#$n,k=map(int,raw_input().split())
l=map(int,raw_input().split())
ans=[0]
cnt,chk=l[-1],1
for i in l[-2::-1]:
    if i<=cnt and chk:
        chk=0
        ans.append(cnt-i+1)
    elif i<=cnt:
        ans.append(cnt-i+1)
    else:
        chk=1
        cnt=i
        ans.append(0)

print ' '.join(map(str,ans[::-1]))


#end = time.clock()
#print end - start
