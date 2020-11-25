#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


mod=10**9+7
t=int(input())
for i in range(t):
    n=int(input())
    l=[int(i) for i in input().split()]
    d=[]
    f=0
    for j in l:
        if f==0 or j!=d[-1]:
            d.append(j)
            f=1
    w={}
    for j in d:
        if j in w: w[j]+=1
        else: w[j]=1
    if len(d)==1:
        print(0)
    elif len(w)==n:
        print(1)
    elif d[0]==d[-1] and w[d[0]]==2:
        print(1)
    else:
        ans=chk=mod
        for j in w:
            x=w[j]-1
            if d[0]!=j: x+=1
            if d[-1]!=j: x+=1
            ans=min(ans,x)
        print(ans)
