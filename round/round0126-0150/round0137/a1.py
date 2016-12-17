#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n,k=map(int,raw_input().split())
l=[int(x) for x in raw_input().split()]
if len(set(l[k-1:]))!=1:
    print -1
    exit()
ans=chk=k-1
for i in range(k-2,-1,-1):
    if l[i]==l[k-1]:
        ans-=1
    else:
        break
print ans
