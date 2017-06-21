#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
a.sort()
for i in range(n-2):
    if a[i]+a[i+1]>a[i+2]:
        print('YES')
        exit()
print('NO')
