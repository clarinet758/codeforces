#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

import heapq
n=int(input())
l=[int(i) for i in input().split()]
syu={}
ich=[]
d={i for i in range(1,n+1)}
for a,i in enumerate(l):
    if i in syu:
        syu[i]+=1
    else:
        syu[i]=1
        heapq.heappush(ich,i)
while len(ich):
    tmp=heapq.heappop(ich)
    if tmp<l[tmp-1]:
        syu[tmp]+=syu[l[tmp-1]]
        syu[l[tmp-1]]=0
ans=0
for i in syu:
    if syu[i]>0:
        ans+=1
print(ans)
