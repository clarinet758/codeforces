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

n=int(raw_input())
#n,k=map(int,raw_input().split())
l=map(int,raw_input().split())
r=l[::-1]
tmp=min(l)
cnt=chk=0
for i in l:
    if i>tmp:
        cnt+=1
    else:
        chk=max(chk,cnt)
        cnt=0
chk=max(chk,cnt)
chk=max(chk,l.index(tmp)+r.index(tmp))
print n*tmp+chk

#end = time.clock()
#print end - start
