#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n=int(input())
chk=0
for i in range(1,n+1):
    if i*i>n:
        break
    elif n%i==0:
        chk=i
ans=[min(chk,n//chk),max(chk,n//chk)]
print(*ans)
