#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
l=map(int,raw_input().split())
ans=chk=1
tmp=-1
for i in l:
    if tmp==-1:
        pass
    elif i>tmp:
        chk+=1
    else:
        chk=1
    tmp=i 
    ans=max(ans,chk)
print ans
