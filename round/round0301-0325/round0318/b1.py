#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
import collections
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.141592653589
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

#n=int(raw_input())
#n,k=map(int,raw_input().split())
#l=map(int,raw_input().split())
ans=chk=0
#end = time.clock()
#print end - start


def sol(i,uni,ans):
    tansaku=uni[i[0]]+uni[i[1]]

    tmp=set([x for x in tansaku if tansaku.count(x)>1])
    if len(tmp)==0:
        return -1
    kaeshi=-1
    for j in tmp:
        if ans!=-1 and len(uni[i[0]])+len(uni[i[1]])>=ans+4:
            break
        if kaeshi==-1:
            kaeshi=(len(uni[i[0]])+len(uni[i[1]])+len(uni[j])-6)
        else:
            kaeshi=min(kaeshi,len(uni[i[0]])+len(uni[i[1]])+len(uni[j])-6)
    return kaeshi
    
N,Q=map(int,raw_input().split())
l=[]
uni={}
for i in range(Q):
    a,b=map(int,raw_input().split())
    l.append((min(a-1,b-1),max(a-1,b-1)))
    if uni.has_key(a-1):
        uni[a-1].append(b-1)
    else:
        uni[a-1]=[b-1]
    if uni.has_key(b-1):
        uni[b-1].append(a-1)
    else:
        uni[b-1]=[a-1]
ans-=1
l.sort()
for i in l:
    m=sol(i,uni,ans)
    if m!=-1 and ans==-1:
        ans=m
    elif m!=-1:
        ans=min(ans,m)
print ans

