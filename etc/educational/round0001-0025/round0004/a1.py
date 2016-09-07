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
n,p,q=map(int,raw_input().split())
s=raw_input()
p,q=max(p,q),min(p,q)
l=[n/p,0]
if n%p==0:
    print l[0] 
    for i in range(l[0]):
        print s[:p]
        s=s[p:]
    exit()
else:
    chk=n%p
    for i in range(l[0]+1):
        if chk%q==0:
            print l[0]+chk/q

            for i in range(l[0]):
                print s[:p]
                s=s[p:]
            for i in range(chk/q):
                print s[:q]
                s=s[q:]
            exit()
        chk+=p
        l[0]-=1
    print -1


#l=map(int,raw_input().split())
ans=chk=0
#end = time.clock()
#print end - start
