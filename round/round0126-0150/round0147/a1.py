#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-
import collections

n=int(input())
d=collections.defaultdict(int)
ans=chk=1
for i in range(n):
    k=input()
    d[k]+=1
    ans=max(ans,d[k])
print(ans)
