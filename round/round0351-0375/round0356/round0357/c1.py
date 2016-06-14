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

n=int(raw_input())
#n,k=map(int,raw_input().split())
#l=map(int,raw_input().split())
l=[]
for i in range(n):
    a=map(str,raw_input().split())
    l.append(a)
cnt=chk=0
ans=[]
for i in l:
    if i[0][0]=='i':
        ans.append(' '.join(i))
        cnt+=1
    elif i[0][0]=='r':
        ans.append(str(i[0]))
        if cnt>0:
            cnt-=1
    elif i[0][0]=='g':
        if cnt>0:
            for j in range(cnt):
                ans.append('removeMin')
        ans.append('insert %s'%i[1])
        ans.append(' '.join(i))
print len(ans)
for i in ans:
    print i
#end = time.clock()
#print end - start
