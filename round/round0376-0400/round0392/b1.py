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
ans=[0]*4
ls=[0]*4
chk={'R':-1,'G':-1,'B':-1,'Y':-1}
h={i:'' for i in range(4)}

n=input()
for a,i in enumerate(n):
    if i=='R':
        chk[i]=a%4
        ls[a%4]=1
        h[a%4]=i
    elif i=='G':
        chk[i]=a%4
        ls[a%4]=1
        h[a%4]=i
    elif i=='B':
        chk[i]=a%4
        ls[a%4]=1
        h[a%4]=i
    elif i=='Y':
        chk[i]=a%4
        ls[a%4]=1
        h[a%4]=i
for i in chk:
    if chk[i]==-1:
        for j in range(4):
            if ls[j]==0:
                chk[i]=j
                h[j]=i
                break
for a,i in enumerate(n):
    if i!=h[a%4]:
        if h[a%4]=='R':
            ans[0]+=1
        elif h[a%4]=='B':
            ans[1]+=1
        elif h[a%4]=='Y':
            ans[2]+=1
        elif h[a%4]=='G':
            ans[3]+=1

print(*ans)

