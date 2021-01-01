#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    x="2020"
    ans=[0]*4
    a=0
    b=n-1
    for p in range(4):
        if s[p]==x[p]:
            ans[p]=1
        else:
            break
    for p in range(4):
        if s[b]==x[3-p]:
            ans[3-p]=1
        else:
            break
        b-=1
    print("YES" if sum(ans)==4 else "NO")
