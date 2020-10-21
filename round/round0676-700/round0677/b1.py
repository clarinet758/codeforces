#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

t=int(input())
for i in range(t):
    ans=f=0
    n=int(input())
    a=[int(i) for i in input().split()]
    while  a[-1]==0:
        a.pop()
    for i in a:
        if i==1: f=1
        if f==1 and i==0: ans+=1
    print(ans)
        
            

