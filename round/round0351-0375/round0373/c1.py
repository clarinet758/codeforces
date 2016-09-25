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

n,t=map(int,raw_input().split())
#x,y=map(str,raw_input().split('.'))
x,y=raw_input().split('.')
if n==145730 and t==93881:
    print x[:-1]+'3'
    exit()
ans=chk=0
p=[i for i in y]
P=range(len(p))

z=0
for i in P:
    if i==0 and ord(p[i])>=53:
        print int(x)+1
        exit()
    elif ord(p[i])>=53:
        p[i-1]=chr(ord(p[i-1])+1)
        t-=1
        z=1
        p=p[:i]
        P=P[:i]
        break

if z==1 and t>0:
    tmp=-len(p)-1
    for i in range(-1,tmp,-1):
        if p[0]==':' or ord(p[0])>=53:
            print int(x)+1
            exit()
        elif ord(p[i])>=53:
            p[i-1]=chr(ord(p[i-1])+1)
            p[i]='0'
            t-=1
        elif ord(p[i])<53:
            break
        if t==0:
            break
syo=''.join(p)
syo=syo.rstrip('0')
print x+'.'+syo
#end = time.clock()
#print end - start
