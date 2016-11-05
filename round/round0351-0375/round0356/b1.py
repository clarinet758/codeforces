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
IS=float('inf')
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

#n=int(raw_input())
n,a=map(int,raw_input().split())
t=map(int,raw_input().split())
ans=chk=0
if t[a-1]==1:
    ans+=1
a-=1
for i in range(1,n+1):
    if a-i<0 and a+i>=n:
        break
    if a-i>=0 and a+i<n:
        if t[a-i]==1 and t[a+i]==1:
            ans+=2
    elif a-i>=0:
        if t[a-i]==1:
            ans+=1
    elif a+i<n:
        if t[a+i]==1:
            ans+=1
print ans

#end = time.clock()
#print end - start
