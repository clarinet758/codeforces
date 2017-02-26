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

ans=0
n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
x={i:0 for i in range(1,6)}
y={i:0 for i in range(1,6)}
for i in a:
    x[i]+=1
for i in b:
    y[i]+=1
ans=[0]*2
for i in range(1,6):
    tmp=x[i]-y[i]
    if tmp%2!=0:
        print(-1)
        exit()
    elif tmp>0:
        ans[1]+=tmp
    else:
        ans[0]+=tmp
print(ans[1]//2 if sum(ans)==0 else -1)

