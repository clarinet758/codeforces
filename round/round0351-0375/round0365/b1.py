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
def niten(a,b): return abs(a-b) if a>=0 and b>=0 else  a+abs(b) if a>=0 else abs(a)+b if b>=0 else abs(abs(a)-abs(b))
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

## TLE

#n=int(raw_input())
n,k=map(int,raw_input().split())
c=map(int,raw_input().split())
chk=sum(c)
#c={a+1:i for a,i in enumerate(map(int,raw_input().split()))}
d=set(map(int,raw_input().split()))
ans=0
for a,i in enumerate(c):
    if a+1 in d:
        ans+=i*(chk-c[a])
    elif (a==0 and n not in d) or a not in d:
        ans+=c[a]*c[a-1]
while 1:
    if len(d)==1:
        break
    tmp=d.pop()
    for i in d:
        ans-=c[tmp-1]*c[i-1]
print ans

#end = time.clock()
#print end - start
