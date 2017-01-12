#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-
import sys
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
pi=3.1415926535897932
IS=float('inf')
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
def niten(a,b): return abs(a-b) if a>=0 and b>=0 else  a+abs(b) if a>=0 else abs(a)+b if b>=0 else abs(abs(a)-abs(b))
def fib(n): return [(seq.append(seq[i-2] + seq[i-1]), seq[i-2])[1] for seq in [[0, 1]] for i in range(2, n)]
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def eucl(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0
def pscl(num,l=[1]):
    for i in range(num):
        l = map(lambda x,y:x+y,[0]+l,l+[0])
    return l

s=input()
t=input()
if s==t:
    print(0)
else:
    d={}
    for i in range(len(s)):
        if s[i] not in d and t[i] not in d:
            d[s[i]]=t[i]
            d[t[i]]=s[i]
        elif (s[i] in d and d[s[i]]!=t[i]) or (t[i] in d and d[t[i]]!=s[i]):
            print(-1)
            exit()
    ans=set([])
    for i in d:
        if i!=d[i]:
            if ord(i)<ord(d[i]):
                ans.add((i,d[i]))
            else:
                ans.add((d[i],i))
    print(len(ans))
    for i in ans:
        print(i[0],i[1])
