#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
l=[int(i) for i in input().split()]
l.sort()
print(l[n//2])
