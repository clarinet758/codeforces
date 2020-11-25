#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

t=int(input())
for i in range(t):
    n=int(input())
    l=[0]*n
    for i in range(n):
        l[(i+1)%n]=i+1
    print(*l)
