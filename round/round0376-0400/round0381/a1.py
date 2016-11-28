#!/usr/bin/env python
# -*- coding: UTF-8 -*-

IS=float('inf')

n,a,b,c=map(int,raw_input().split())
if n%4==0:
    print 0
    exit()
ans=chk=IS
for i in range(10):
    for j in range(10):
        for k in range(10):
            if (n+i+j*2+k*3)%4==0:
                ans=min(ans,i*a+j*b+k*c)
print ans
