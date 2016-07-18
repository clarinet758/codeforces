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

s=raw_input()
n=int(raw_input())
for i in range(n):
    t=s
    l,r,k=map(int,raw_input().split())
    tmp=s[l-1:r]
    x=((k%len(tmp)))*-1
    tmp=tmp[x:]+tmp[:x]
    s=t[:l-1]+tmp+t[r:]
print s
#n,k=map(int,raw_input().split())
#print t,tmp
ans=chk=0
#end = time.clock()
#print end - start
