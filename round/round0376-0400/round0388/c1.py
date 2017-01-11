#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

import heapq
n=int(input())
s=input()
r,d=[],[]
for a,i in enumerate(s):
    if i=='R':
        heapq.heappush(r,a)
    else:
        heapq.heappush(d,a)
while len(r) and len(d):
    R=heapq.heappop(r)
    D=heapq.heappop(d)
    if R<D:
        heapq.heappush(r,R+n)
    else:
        heapq.heappush(d,D+n)
print(['R','D'][len(d)>0])
