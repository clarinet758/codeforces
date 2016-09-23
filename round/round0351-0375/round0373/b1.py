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

n=int(raw_input())
s=raw_input()
#n,k=map(int,raw_input().split())
#l=map(int,raw_input().split())
t1=t2=t3=t4=0
if n%2 or n%2==0:
    for a,i in enumerate(s):
        if a%2 and i=='r':
            t2+=1
        elif a%2==0 and i=='b':
            t1+=1
    chk=abs(t2-t1)+min(t2,t1)
    for a,i in enumerate(s):
        if a%2 and i=='b':
            t3+=1
        elif a%2==0 and i=='r':
            t4+=1
    print min(chk,abs(t3-t4)+min(t3,t4))
else:
    for a,i in enumerate(s):
        if (a%2 and a<=n/2-1 and i=='r') or (a==n/2 and i=='r') or (a%2==0 and a>n/2 and i=='r'):
            t2+=1
        elif (a%2==0 and a<=n/2 and i=='b') or (a%2==1 and a>n/2 and i=='b'):
            t1+=1
    chk=abs(t2-t1)+min(t2,t1)
    for a,i in enumerate(s):
        if (a%2 and a<=n/2-1 and i=='b') or (a==n/2 and i=='b') or (a%2==0 and a>n/2 and i=='b'):
            t3+=1
        elif (a%2==0 and a<=n/2 and i=='r') or (a%2==1 and a>n/2 and i=='r'):
            t4+=1
    print min(chk,abs(t3-t4)+min(t3,t4))



#end = time.clock()
#print end - start
