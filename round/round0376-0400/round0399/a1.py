#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n=int(input())
l=[int(i) for i in input().split()]
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
s=set(l)
print(max(n-d[min(s)]-d[max(s)],0))
