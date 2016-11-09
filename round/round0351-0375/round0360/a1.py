#!/usr/bin/env python
# -*- coding: UTF-8 -*-

ans=chk=0
n,d=map(int,raw_input().split())
for i in range(d):
    if '0' in raw_input():
        chk+=1
        ans=max(ans,chk)
    else:
        chk=0
print ans

