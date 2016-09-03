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

n,s=map(int,raw_input().split())
l=[0]*(s+1)
for i in range(n):
    a,b=map(int,raw_input().split())
    l[a]=max(l[a],b)
ans=0
for i in l[::-1]:
    if i>ans:
        ans=i
    ans=ans+1
print ans-1
#l=map(int,raw_input().split())
ans=chk=0
#end = time.clock()
#print end - start
