#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

t=int(input())
for i in range(t):
    n=int(input())
    l=[int(i) for i in input().split()]
    f=1
    a=0
    b=n-1
    ans=[]
    for i in range(n):
        if f:
            ans.append(l[a])
            a+=1
        else:
            ans.append(l[b])
            b-=1
        f=(f+1)%2
    print(*ans)

