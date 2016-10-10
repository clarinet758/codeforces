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
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

n=int(raw_input())
#n,k=map(int,raw_input().split())
l=map(int,raw_input().split())
ans=chk=d=p=q=0
s=raw_input()
A=B=0
for a,i in enumerate(s):
    if i=='B':
        d+=l[a]
ans=p=d
for a,i in enumerate(s):
    if i=='B':
        p-=l[a]
    else:
        p+=l[a]
    ans=max(ans,p)
h=l[::-1]
q=d
for a,i in enumerate(s[::-1]):
    if i=='B':
        q-=h[a]
    else:
        q+=h[a]
    ans=max(ans,q)
print ans


#end = time.clock()
#print end - start
