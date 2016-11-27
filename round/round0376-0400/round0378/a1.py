#!/usr/bin/env python
# -*- coding: UTF-8 -*-

s=raw_input()
chk='AEIOUY'
ans=tmp=1
for i in s:
    if i in chk:
        tmp=1
    else:
        tmp+=1
        ans=max(ans,tmp)
print ans
