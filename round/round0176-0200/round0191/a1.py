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
l=[int(x) for x in raw_input().split()]
ans=chk=0
for i in l:
    if i==0:
        chk+=1
    else:
        chk-=1
    if chk<0:
        chk=0
    ans=max(ans,chk)
print n-1 if 0 not in l else l.count(1)+ans
