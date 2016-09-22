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
#def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

#n=int(raw_input())

#    WA!!!!!!

n,x1,y1,x2,y2=map(int,raw_input().split())
a,b,h=0,0,0
l=r=0
memo=[(0,10**8)]
for i in range(n):
    x,y=map(int,raw_input().split())
    a=euclid_dis(x1,y1,x,y)
    b=euclid_dis(x2,y2,x,y)
    l=max(l,a)
    memo.append((a,b))

memo.sort()
ans=l
#print ans,memo
p=range(-1,-n-1,-1)
for i in p:
#    print memo[i],memo[i-1]
    tmp=memo[i-1][0]+max(r,memo[i][1])
    if tmp<=ans:
#        print l,r
        l=memo[i-1][0]
        r=max(r,memo[i][1])
        ans=tmp
print ans
#end = time.clock()
#print end - start
