#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

from collections import deque
n,l=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
x=deque()
y=deque()
for i in range(n):
    if i==0:
        x.append(a[0]+(l-a[-1]))
    else:
        x.append(a[i]-a[i-1])
for i in range(n):
    if i==0:
        y.append(b[0]+(l-b[-1]))
    else:
        y.append(b[i]-b[i-1])
for i in range(n):
    if x==y:
        print('YES')
        exit()
    tmp=x.popleft()
    x.append(tmp)

print('NO')

