#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
l=[int(i) for i in input().split()]
k=[0]*n
k[0]=1
m=[1,1]
ans=chk=0
if l[0]==0 or sum(l)+1<n:
    print(-1)
    exit()
print(n-1)
for a,i in enumerate(l):
    t=i
    if all(k): break
    for x in range(m[0],n):
        if t==0: break
        if l[x]>0 and k[x]==0:
            k[x]=1
            m[0]=x
            t-=1
            print(a+1, x+1)
    if t==0: continue
    for x in range(m[1],n):
        if t==0: break
        if k[x]==0:
            k[x]=1
            m[1]=x
            t-=1
            print(a+1, x+1)


