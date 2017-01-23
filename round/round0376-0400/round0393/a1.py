#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

m,d=[int(i) for i in input().split()]
m0=[4,6,9,11]
m1=[1,3,5,7,8,10,12]
if m in m0:
    if d==7:
        ans=6
    else:
        ans=5
elif m in m1:
    if d>=6:
        ans=6
    else:
        ans=5
else:
    if d==1:
        ans=4
    else:
        ans=5
print(ans)
