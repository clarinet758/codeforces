#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n=int(input())
l=[int(i) for i in input().split()]
print(max(l)*n-sum(l))
