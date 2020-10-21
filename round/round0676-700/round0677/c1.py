#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

t=int(input())
for i in range(t):
    n=int(input())
    l=[int(i) for i in input().split()]
    if len(set(l))==1:
        print(-1)
    else:
        x=max(l)
        for j in range(n):
            if l[j]==x and (l[j]>l[min(j+1,n-1)] or l[j]>l[max(0,j-1)]):
                print(j+1)
                break

