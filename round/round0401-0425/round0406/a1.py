#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

a,b=map(int,input().split())
c,d=map(int,input().split())
x=y=0
chk=set([])
for i in range(0,700000,1):
    x=b+a*i
    y=d+c*i
    if x==y or (x in chk and y in chk):
        print(min(x,y))
        exit()
    if x in chk:
        print(x)
        exit()
    if y in chk:
        print(y)
        exit()
    chk.add(x)
    chk.add(y)
print(-1)


