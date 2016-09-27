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

n=int(raw_input())
#n,k=map(int,raw_input().split())
l=[0]*1999
r=[0]*1999
memo=[0,0]
p=[1]
for i in range(1001):
    p=map(lambda x,y:x+y,[0]+p,p+[0])
    if i>0:
        memo.append(p[2])


for i in range(n):
    x,y=map(int,raw_input().split())
    l[x-y+999]+=1
    r[x+y-2]+=1
l=[i for i in l if i>1]
r=[i for i in r if i>1]
ans=chk=0
for i in l:
    ans+=memo[i]
for i in r:
    ans+=memo[i]
print ans
#end = time.clock()
#print end - start
