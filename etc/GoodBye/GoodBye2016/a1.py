#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
k=240-k
ans=0
chk=1
while (k-chk*5>=0):
    ans+=1
    k-=chk*5
    chk+=1
print(min(ans,n))
