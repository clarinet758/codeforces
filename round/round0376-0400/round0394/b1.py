#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n,l=map(int,input().split())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
x,y=[],[]

for i in range(n):
    if i==0:
        x.append(a[i]+(l-a[-1]))
    else:
        x.append(a[i]-a[i-1])
for i in range(n):
    if i==0:
        y.append(b[i]+(l-b[-1]))
    else:
        y.append(b[i]-b[i-1])
y=y+y
for i in range(n):
    f=1
    for j in range(n):
        if x[j]!=y[j+i]:
            f=0
    if f:
        print('YES')
        exit()
print('NO')
