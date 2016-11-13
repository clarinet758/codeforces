#!/usr/bin/env python
# -*- coding: UTF-8 -*-

IS=float('inf')
n=int(raw_input())
s=raw_input()
x=map(int,raw_input().split())
l=r=-1
ans=chk=IS
for i in range(n):
    if s[i]=='R':
        r=x[i]
    else:
        if r!=-1:
            ans=min(ans,(x[i]-r)/2)
print ans if ans!=IS else -1
