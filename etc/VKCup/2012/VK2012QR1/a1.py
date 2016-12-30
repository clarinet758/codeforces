#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n,k=map(int,raw_input().split())
l=[int(x) for x in raw_input().split()]
ans=chk=0
for i in range(n):
    if l[i]>=l[k-1] and l[i]>0:
        ans+=1
print ans
