#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n,m,k=map(int,input().split())
a=[int(i) for i in input().split()]
ans=100

for x,i in enumerate(range(m,n,1)):
    if a[i]>0 and a[i]<=k:
        ans=x+1
        break
for y,j in enumerate(range(m-2,-1,-1)):
    if a[j]>0 and a[j]<=k:
        ans=min(ans,y+1)
        break
print(ans*10)
