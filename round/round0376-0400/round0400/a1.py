#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

a,b=input().split()
print(a,b)
n=int(input())
l=[a,b]
for i in range(n):
    a,b=input().split()
    if a==l[0]:
        l[0]=b
    else:
        l[1]=b
    print(*l)
