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
#n=int(raw_input())
n,t=map(int,raw_input().split())
#l=map(int,raw_input().split())
if n==1:
    if t==10:
        print -1
    else:
        print t
else:
    if t==10:
        print '1'+'0'*(n-1)
    else:
        print str(t)+'0'*(n-1)
#end = time.clock()
#print end - start
