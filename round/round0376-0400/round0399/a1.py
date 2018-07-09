#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
n=int(input())
a=[int(i) for i in input().split()]
d={}
ans=0
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
a=list(set(a))
a.sort()
if len(a)<3:
    print(ans)
else:
    for i in range(1,len(a)-1):
        ans+=d[a[i]]
    print(ans)

