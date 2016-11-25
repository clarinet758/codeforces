#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import heapq

n,k=map(int,raw_input().split())
l={}
m=[]
for i in range(n):
    s=raw_input()
    if len(s) in l:
        l[len(s)]+=1
    else:
        l[len(s)]=1
        heapq.heappush(m,len(s))
chk=len(raw_input())
ans=0
cnt=0
while 1:
    tmp=heapq.heappop(m)
    if tmp==chk:
        print (ans/k)*5+ans+1,((ans+l[tmp]-1)/k)*5+ans+l[tmp]
        break
    else:
        ans+=l[tmp]
