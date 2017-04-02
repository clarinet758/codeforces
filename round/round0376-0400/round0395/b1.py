#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n=int(input())
l=[int(i) for i in input().split()]
for i in range(0,n//2,2):
    l[i],l[i*-1-1]=l[i*-1-1],l[i]
print(*l)
