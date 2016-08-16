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
def sinsu(a): pass

def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

#n=int(raw_input())
#def test(a,b,c=0): return c for k,y in enumerate(a[::-1]): c+=(b**k)*int(y)
def sol(k,s):
    t=0
    for a,i in enumerate(s[::-1]):
        t+=i*(k**a)
    return t

n,b=map(int,raw_input().split())
x=map(int,raw_input().split())
n2,b2=map(int,raw_input().split())
y=map(int,raw_input().split())
print '=' if sol(b,x)==sol(b2,y) else '>' if sol(b,x)>sol(b2,y) else '<'
#end = time.clock()
#print end - start
