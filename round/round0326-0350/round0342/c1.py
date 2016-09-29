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

ans=chk=0
n,k=map(int,raw_input().split())
#l=map(int,raw_input().split())
#l=[[0]*n for _ in range(n)]
l=[[] for _ in range(n)]
tmp=0
for i in range(n):
    for j in range(k-1):
        tmp+=1
        l[i].append(tmp)
for i in range(n):
    for j in range(n-k+1):
        tmp+=1
        l[i].append(tmp)
        if j==0:
            ans+=l[i][-1]
print ans
for i in l:
    print ' '.join(map(str,i))



#end = time.clock()
#print end - start
