#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

t=int(input())
for i in range(t):
    a,b,k=map(int,input().split())
    x=[int(i)-1 for i in input().split()]
    y=[int(i)-1 for i in input().split()]
    xd={int(i):0 for i in range(a)}
    yd={int(i):0 for i in range(b)}
    ans=0
    for i in x:
        xd[i]+=1
    for i in y:
        yd[i]+=1
    #print(xd,yd)
    for i in range(k):
        ans+= k-xd[x[i]]-yd[y[i]]+1
    print(ans//2)
