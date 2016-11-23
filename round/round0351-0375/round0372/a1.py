#!/usr/bin/env python
# -*- coding: UTF-8 -*-
n,c=map(int,raw_input().split())
l=map(int,raw_input().split())
ans=chk=0
for i in l:
    if i-chk>c:
        ans=1
    else:
        ans+=1
    chk=i
print ans
