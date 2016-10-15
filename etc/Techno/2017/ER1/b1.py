#!/usr/bin/env python
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
pi=3.141592653589
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

#n=int(raw_input())
s=raw_input()
s+='$'
tmp=''
l=[]
ans=[0]*3
for i in s:
    if i.isdigit() or i=='.':
        tmp+=i
    else:
        if len(tmp):
            l.append(tmp)
        tmp=''
for i in l:
    t=i.split('.')
    if len(t)==3:
        ans[0]+=int(t[0])
        ans[1]+=int(t[1])
        ans[2]+=int(t[2])
    elif len(t)==2 and len(t[1])==3:
        ans[0]+=int(t[0])
        ans[1]+=int(t[1])
    elif len(t)==2:
        ans[1]+=int(t[0])
        ans[2]+=int(t[1])
    else:
        ans[1]+=int(t[0])

ans[1]+=ans[2]/100
ans[2]=ans[2]%100
ans[0]+=ans[1]/1000
ans[1]=ans[1]%1000
p=''
#print ans
if ans[0]>0:
    p=str(ans[0])+'.'
if len(p)>0:
    t=str(ans[1])
    t='0'*(3-len(t))+t
    p+=t
else:
    p=str(ans[1])
if ans[2]!=0:
    t=str(ans[2])
    t='0'*(2-len(t))+t
    p+='.'+t
print p
exit()
n,k=map(int,raw_input().split())
l=map(int,raw_input().split())
ans=chk=0
#end = time.clock()
#print end - start
