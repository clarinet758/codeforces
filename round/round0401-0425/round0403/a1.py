#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n=int(input())
x=[int(i) for i in input().split()]
chk=[0]*(n+1)
ans=tmp=0
for i in x:
    if chk[i]==0:
        chk[i]=1
        tmp+=1
    else:
        chk[i]=0
        tmp-=1
    ans=max(ans,tmp)
print(ans)
