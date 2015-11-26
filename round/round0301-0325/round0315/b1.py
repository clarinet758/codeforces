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
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
#start = time.clock()
n=int(raw_input())
a=map(int,raw_input().split())
l=set(a)
ans=[0]*n
tmp=set(range(1,n+1))
tmp=list(tmp-l)
for i in a:
    if i in l and i<=n:
        print i,
        l.remove(i)
    else:
        print tmp.pop(),



#end = time.clock()
#print end - start
