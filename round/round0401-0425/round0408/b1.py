#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n,m,k=map(int,input().split())
h=set([i for i in input().split()])
ans=chk='1'

while k:
    k=k-1
    if ans in h:
        break
    x,y=map(str,input().split())
    if x==ans:
        ans=y
    elif y==ans:
        ans=x
print(ans)
