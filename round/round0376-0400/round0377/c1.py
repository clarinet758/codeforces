#!/usr/bin/env python
# -*- coding: UTF-8 -*-

l=map(int,raw_input().split())
l.sort()
ans=0
if l[2]!=l[1]:
    ans+=(l[2]-1)-l[1]
if l[2]!=l[0]:
    ans+=(l[2]-1)-l[0]
print ans
