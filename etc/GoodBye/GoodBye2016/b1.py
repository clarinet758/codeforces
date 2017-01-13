#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n=int(input())
ans=chk=0
for i in range(n):
    t,d=map(str,input().split())
    t=int(t)
    if (chk==0 and d=='South' and t<=20000):
        chk+=t
    elif (chk==0):
        ans=1
    elif (chk==20000 and d=='North' and t<=20000):
        chk-=t
    elif (chk==20000):
        ans=1
    elif (d=='North' and chk-t>=0):
        chk-=t
    elif (d=='North'):
        ans=1
    elif (d=='South' and chk+t<=20000):
        chk+=t
    elif (d=='South'):
        ans=1
if chk==0 and ans==0:
    print('YES')
else:
    print('NO')
