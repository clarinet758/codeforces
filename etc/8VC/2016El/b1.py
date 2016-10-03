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
s=raw_input()
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
if len(d)==1:
    for i in d:
        print i
elif len(d)==3:
    print 'BGR'
else:
    tmp=[]
    for i in d:
        tmp.append(i)
    if d[tmp[0]]==d[tmp[1]]==1:
        print 'RGB'.replace(tmp[0],'').replace(tmp[1],'')
    elif d[tmp[0]]==1 or d[tmp[1]]==1:
        ch='RGB'.replace(tmp[0],'').replace(tmp[1],'')
        tw=[i for i in d if d[i]==1]
        tw.append(ch)
        tw.sort()
        print ''.join(tw)
    else:
        print 'BGR'

exit()
n,k=map(int,raw_input().split())
l=map(int,raw_input().split())
ans=chk=0
#end = time.clock()
#print end - start
