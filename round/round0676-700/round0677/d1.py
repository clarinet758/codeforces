#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

t=int(input())
for i in range(t):
    n=int(input())
    l=[int(i) for i in input().split()]
    if len(set(l))==1:
        print("NO")
    else:
        print("YES")
        p=[0,l[0]]
        for j in range(n):
            if l[j]!=p[1]:
                q=[j,l[j]]
                break
        print(1,q[0]+1)
        for j in range(1,n):
            if j==q[0]:
                continue
            if l[j]==p[1]:
                print(j+1,q[0]+1)
            else:
                print(j+1,1)
            
