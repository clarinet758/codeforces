#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-
import heapq

n,k=[int(i) for i in input().split()]
l=[int(i) for i in input().split()]
cnt=[i for i in l if i<0]
m=0
for a,i in enumerate(l):
    if i<0 and m==0:
        m=1
    elif i<0 and l[a-1]>=0:
        m+=1
d={}
q=[]
chk=-1
for i in l:
    if i<0:
        if chk>0:
            if chk in d:
                d[chk]+=1
            else:
                d[chk]=1
                heapq.heappush(q,chk)
        chk=0
    elif chk>=0:
        chk+=1
ans=m*2
k-=len(cnt)
while len(q) and k>=q[0]:
    k-=q[0]
    ans-=2
    d[q[0]]-=1
    if d[q[0]]==0:
        heapq.heappop(q)
if k>=chk and chk>-1:
    ans-=1
print(ans if ans>=0 and k>=0 else -1)
