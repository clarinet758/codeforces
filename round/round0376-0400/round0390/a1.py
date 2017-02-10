#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
if a.count(0)==n:
    print('NO')
elif sum(a)!=0:
    print('YES',1,sep='\n')
    print(1,n)
else:
    print('YES',2,sep='\n')
    for i in range(1,n):
        if sum(a[:i]):
            print(1,i)
            print(i+1,n)
            break
