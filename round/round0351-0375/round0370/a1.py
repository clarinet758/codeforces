#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
b=[]
e=o=0
a=map(int,raw_input().split())
for i,j in enumerate(a[::-1]):
    if i%2==0:
        tmp=j-(e-o)
        e+=tmp
    else:
        tmp=j-(o-e)
        o+=tmp
    b.append(str(tmp))
print ' '.join(b[::-1])
