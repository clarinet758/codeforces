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
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

#n=int(raw_input())
n,s=map(int,raw_input().split())
d={}
for i in range(n):
    f,t=map(int,raw_input().split())
    if d.has_key(f):
        d[f]=max(d[f],t)
    else:
        d[f]=t
ans=chk=0
while s:
    if d.has_key(s):
        ans=max(ans,d[s])
    s-=1
    ans+=1
print ans
#end = time.clock()
#print end - start
