#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
p=map(int,raw_input().split())
t='aeiouy'
for i in range(n):
    s=raw_input()
    tmp=0
    for j in t:
        tmp+=s.count(j)
    if tmp!=p[i]:
        print 'NO'
        exit()
print 'YES'

n,k=map(int,raw_input().split())
