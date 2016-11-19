#!/usr/bin/env python
# -*- coding: UTF-8 -*-

IS=float('inf')

n,m,k=map(int,raw_input().split())
d=[]
for i in range(m):
    d.append(map(int,raw_input().split()))
if k:
    a=set(map(int,raw_input().split()))
else:
    a=set([])
ans=chk=IS
for u,v,c in d:
    if len(a&set([u,v]))==1:
        ans=min(ans,c)
print ans if ans!=IS else -1
