#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-


n,m=[int(i) for i in input().split()]
p,e=set([]),set([])
for i in range(n):
    p.add(input())
for i in range(m):
    e.add(input())
tyo=p&e
n-=len(tyo)
m-=len(tyo)

if n>m or (len(tyo)%2 and n==m):
    print('YES')
else:
    print('NO')
