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
if sum(l)==0:
    print 0
    exit()
cnt=[]
chk=f=0
for i in l:
    if i==1 and f==0:
        f=1
        chk=1
    elif i==1 and f==1:
        cnt.append(chk)
        chk=1
    elif i==0 and f==1:
        chk+=1
ans=1
for i in cnt:
    ans*=i
print ans
#end = time.clock()
#print end - start
