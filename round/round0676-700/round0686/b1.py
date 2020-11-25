#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


mod=1000000007
t=int(input())
for i in range(t):
    n=int(input())
    ans=chk=mod
    l=[int(i) for i in input().split()]
    w={}
    ans=chk=mod
    for j,k in enumerate(l):
        if k not in w:
            w[k]=j
        else:
            w[k]=-1
    for j in w:
        if w[j]>-1 and chk>j:
            chk=j
            ans=w[j]
            
    print(ans+1 if chk!=mod else -1)
