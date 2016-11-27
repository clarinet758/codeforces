#!/usr/bin/env python
# -*- coding: UTF-8 -*-

s=raw_input()
chk=ord('a')
ans=0
for i in s:
    tmp=abs(ord(i)-chk)
    ans+=min(tmp,26-tmp)
    chk=ord(i)
print ans
