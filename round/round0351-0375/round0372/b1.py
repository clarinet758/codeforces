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

s=raw_input()
if len(s)<26:
    print -1
    exit()
for i in range(len(s)-25):
    tmp=''
    l=set([chr(x+ord('A')) for x in range(26)])
    f=0
    for j in range(26):
        if s[i+j] in l:
            l.remove(s[i+j])
            tmp+=s[i+j]
        elif s[i+j]=='?':
            tmp+='?'
        else:
            f=1
            break
    if f==0:
        ans=s[:i]
        for z in tmp:
            if z=='?':
                ans+=l.pop()
            else:
                ans+=z
        ans+=s[i+26:]
        ans=ans.replace('?','A')
        print ans
        exit()
print -1



