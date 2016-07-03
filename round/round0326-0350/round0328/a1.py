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
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

#n=int(raw_input())
l=[]
s=[[''] for i in range(8)]
for i in range(8):
    l.append(raw_input())
A=B=8
for i in range(8):
    for j in range(8):
        s[i][0]+=l[j][i]
for i in s:
    a=b=-1
    if 'B' in i[0]:
        for j in i[0]:
            if j=='B':
                b=0
            elif j=='.' and b!=-1:
                b+=1
            elif b!=-1 and j=='W':
                b=-1
        if b!=-1: B=min(b,B)
    if 'W' in i[0]:
        for j in i[0][::-1]:
            if j=='W':
                a=0
            elif j=='.' and a!=-1:
                a+=1
            elif a!=-1 and j=='B':
                a=-1
        if a!=-1: A=min(a,A)
print 'A' if A==min(A,B) else 'B'
#n,k=map(int,raw_input().split())
#l=map(int,raw_input().split())
ans=chk=0
#end = time.clock()
#print end - start
