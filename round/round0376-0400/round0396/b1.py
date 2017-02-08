#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
a.sort()
f=0
for i in range(n-2):
    if a[i]+a[i+1]>a[i+2]:
        f=1
print('YES' if f else 'NO')
