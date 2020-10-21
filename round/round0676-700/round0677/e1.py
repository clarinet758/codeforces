#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
x=y=1
for i in range(n,0,-1):
    x*=i
print(x//((n//2)**2)//2)
