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

#n=int(input())
n,k=[int(i) for i in input().split()]
l=[0]*300002
memo=[]
for i in range(n):
    a,b=[int(i) for i in input().split()]
    memo.append((a,b))
    l[a]+=1
    l[b+1]-=1
ans=chk=now=cnt=0
fas=fae=0
mes=mee=0
for i in range(1,300002):
    now+=l[i]
    if now>=k:
        cnt+=1
        if mes==0:
            mes=i
    elif now<k:
        if cnt>ans:
            ans=cnt
            fas=mes
            fae=i-1
        cnt=0
        mes=0
if ans==0:
    print(0)
    tmp0=[int(i) for i in range(1,k+1)]
    print(*tmp0)
else:
    print(ans)
    tmp1=[]
    for a,i in enumerate(memo):
        if fas>=i[0] and fae<=i[1]:
            tmp1.append(a+1)
            k-=1
            if k==0:
                break
    print(*tmp1)
