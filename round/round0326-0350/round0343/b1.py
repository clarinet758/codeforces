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
def eucl(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0
def pscl(num,l=[1]):
    for i in range(num):
        l = map(lambda x,y:x+y,[0]+l,l+[0])
    return l


n=int(raw_input())
f=[0]*368
m=[0]*368
for i in range(n):
    x,a,b=map(str,raw_input().split())
    if x=='F':
        f[int(a)]+=1
        f[int(b)+1]-=1
    else:
        m[int(a)]+=1
        m[int(b)+1]-=1
ans=chk=0
f2=m2=0
for i in range(368):
    f2+=f[i]
    m2+=m[i]
    ans=max(ans,min(f2,m2)*2)
print ans
exit()
l=map(int,raw_input().split())
#end = time.clock()
#print end - start
