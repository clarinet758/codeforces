#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
l=[int(i) for i in input().split()]
ans=[]
for i in l:
    ans.append((i+k-1)//k)
print((sum(ans)+1)//2)
