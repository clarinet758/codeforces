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
a,b=[0],[0]*6
for i in s:
    if i.isdigit() or i=='.':
        tmp+=i
    else:
        if len(tmp):
            l.append(tmp)
        tmp=''
for i in l:
    t=i.split('.')
    if len(t)==1:
        b[0]+=int(t[0])
    elif len(t)>1:
        if len(t[-1])==2:
            a[0]+=int(t[-1])
            for p,j in enumerate(t[::-1]):
                if p>0:
                    b[p-1]+=int(j)
        else:
            for p,j in enumerate(t[::-1]):
                b[p]+=int(j)
b[0]+=a[0]/100
a[0]=a[0]%100
for p,i in enumerate(b):
    if p<4:
        b[p+1]+=b[p]/1000
        b[p]=b[p]%1000
while 1:
    if b[-1]==0 and len(b)>1:
        b.pop(-1)
    else:
        break
ans=''
for i in b[::-1]:
    if ans=='':
        ans=str(i)
    else:
        tmp=str(i)
        tmp='0'*(3-len(tmp))+tmp
        ans+='.'+tmp
if a[0]>0:
    tmp=str(a[0])
    if len(tmp)==1:
        ans+='.'+'0'+tmp
    else:
        ans+='.'+tmp
print ans
    

exit()


n,k=map(int,raw_input().split())
l=map(int,raw_input().split())
ans=chk=0
#end = time.clock()
#print end - start
