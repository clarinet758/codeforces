#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
l=[int(i) for i in input().split()]
ans=[]

chkl=0
for i in l[::-1]:
    if i>chkl:
        ans.append(i)
        chkl=i
    else:
        ans.append(0)
res=[]
t=0
for i in ans:
    if i!=0:
        res.append(list(range(i,t,-1)))
        t=i
    else:
        res.append(0)
for i in res[::-1]:
    if i==0:
        print()
    else:
        print(*i)
