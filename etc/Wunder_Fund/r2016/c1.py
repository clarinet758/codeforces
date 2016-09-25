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
def euclid(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

n=int(raw_input())
a,b=map(int,raw_input().split())
c,d=map(int,raw_input().split())
chk=[[a,b,1],[c,d,2],[]]
l=[[c,d,2]]
memo=euclid(a,b,c,d)
for i in range(n-2):
    x,y=map(int,raw_input().split())
    l.append([x,y,i+3])
    t=euclid(a,b,x,y)
    if t<memo:
        chk[1]=[x,y,i+3]
        memo=t
t=IS
for i in l:
    a=chk[1][0]-chk[0][0]
    b=chk[1][1]-chk[0][1]
    c=i[0]-chk[0][0]
    d=i[1]-chk[0][1]
    tmp=abs(a*d-b*c)
    if tmp>0 and tmp<t:
        chk[2]=i
        t=tmp
print chk[0][2],chk[1][2],chk[2][2]
#l=map(int,raw_input().split())
ans=chk=0
#end = time.clock()
#print end - start
