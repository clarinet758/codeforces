#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

#import heapq
from collections import deque
n=int(input())
s=input()
r,d=deque(),deque()
for a,i in enumerate(s):
    if i=='R':
        r.appendleft(a)
    else:
        d.appendleft(a)
while len(r) and len(d):
    R=r.pop()
    D=d.pop()
    if R<D:
        r.appendleft(R+n)
    else:
        d.appendleft(D+n)
print(['R','D'][len(d)>0])
