#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n,m=map(int,raw_input().split())
a=map(int,raw_input().split())
x=[0]*(n+1)
x[1]+=a[0]
ans=chk=0
for i in range(1,n):
    x[i+1]=x[i]+a[i]
for i in range(m):
    l,r=map(int,raw_input().split())
    ans+=max(0,x[r]-x[l-1])
print ans
