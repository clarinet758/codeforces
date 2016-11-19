#!/usr/bin/env python
# -*- coding: UTF-8 -*-

IS=float('inf')
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5

ans=chk=IS
a,b=map(int,raw_input().split())
n=int(raw_input())
for i in range(n):
    x,y,v=map(int,raw_input().split())
    chk=euclid_dis(a,b,x,y)
    ans=min(ans,chk/v)
print '{0:.10f}'.format(ans)
