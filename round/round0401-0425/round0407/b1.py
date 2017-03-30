#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

b1,q,l,m=map(int,input().split())
a=set([int(i) for i in input().split()])
a.add(l)
if abs(b1)>=l:
    print(0)
    exit()
if b1==0:
    if 0 in a:
        print(0)
    else:
        print('inf')
    exit()
if q==1:
    if b1 in a:
        print(0)
    else:
        print('inf')
    exit()
if q==-1:
    if b1 in a and b1*q in a:
        print(0)
    else:
        print('inf')
    exit()
if q==0:
    if b1 in a and 0 in a:
        print(0)
    elif 0 in a:
        print(1)
    else:
        print('inf')
    exit()

tmp=b1
ans=0
while 1:
    if abs(tmp)>=l:
        break
    elif tmp not in a:
        ans=ans+1
    tmp=tmp*q
print(ans)
