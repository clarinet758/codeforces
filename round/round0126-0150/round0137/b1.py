#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# TLE解決できず

n,m,k=map(int,raw_input().split())
l=[]
x={i:i for i in range(n)}
y={i:i for i in range(m)}
for i in range(n):
    l.append(raw_input().split())
for i in range(k):
    a,b,c=map(str,raw_input().split())
    b=int(b)
    c=int(c)
    if a=='g':
        print l[x[b-1]][y[c-1]]
    elif a=='r':
        x[b-1],x[c-1]=x[c-1],x[b-1]
    else:
        y[b-1],y[c-1]=y[c-1],y[b-1]
        
