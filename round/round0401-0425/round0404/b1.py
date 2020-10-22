#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


n=int(input())
p=[0,10**10]
q=[0,10**10]
for i in range(n):
    a,b=map(int,input().split())
    p[0]=max(p[0],a)
    p[1]=min(p[1],b)
m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    q[0]=max(q[0],a)
    q[1]=min(q[1],b)
print(max(0,q[0]-p[1],p[0]-q[1]))
