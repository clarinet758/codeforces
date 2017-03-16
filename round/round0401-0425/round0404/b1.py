#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

nn,mm=[],[]
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if i==0:
        nn.append((a,b))
        nn.append((a,b))
    elif b<nn[0][1]:
        nn[0]=(a,b)
    elif a>nn[1][0]:
        nn[1]=(a,b)

m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    if i==0:
        mm.append((a,b))
        mm.append((a,b))
    elif b<mm[0][1]:
        mm[0]=(a,b)
    elif a>mm[1][0]:
        mm[1]=(a,b)
ans=max(0,mm[1][0]-nn[0][1],nn[1][0]-mm[0][1])
print(ans)
