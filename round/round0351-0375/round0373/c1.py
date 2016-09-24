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

#n=int(raw_input())
n,t=map(int,raw_input().split())
x,y=map(str,raw_input().split('.'))
ans=chk=0
#if len(y)<n+1:
if len(y)<t+1:
    y+='0'*((t+1)-len(y))
#elif len(y)>n+1:
#    y=y[:n+1]
p=[int(i) for i in y]
f=0
tmp1=0
while t:
    z=0
    for i in range(len(p)):
        if i==0 and p[i]>=5:
            f+=1
            p[0]=0
            t-=1
            z=1
            tmp1=i
            p=p[:0+1]
            break
        elif p[i]>=5:
            p[i]=0
            p[i-1]+=1
            t-=1
            z=1
            tmp1=i
            p=p[:i+1]
            break
    if z==0:
        break
    for i in range(-1,-len(p)-1,-1):
        if p[i]==10:
            p[i-1]+=1
            p[i]=0
sei=int(x)+f
p=p[:tmp1+1]
syo=''.join(map(str,p))
syo=int(syo)
if syo==0:
    print sei
else:
    syo=str(syo).rstrip('0')
    print str(sei)+'.'+syo
#end = time.clock()
#print end - start
