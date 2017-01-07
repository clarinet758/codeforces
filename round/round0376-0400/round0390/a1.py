#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n=int(input())
l=[int(i) for i in input().split()]
ans=chk=0
if sum(l)==0 and len(l)==1:
    print('NO')
    exit()
else:
    if sum(l)==0 and l.count(0)==n:
        print('NO')
    elif sum(l)!=0:
        print('YES')
        print(1)
        print(1,n)

    else:
        for i in range(1,n):
            if sum(l[:i])!=0 and sum(l[i:]):
                print('YES')
                print(2)
                print(1,i)
                print(i+1,n)
                exit()

