#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

s,x1,x2=[int(i) for i in input().split()]
t1,t2=[int(i) for i in input().split()]
p,d=[int(i) for i in input().split()]

ig=abs(x1-x2)*t2
tr=0
while 1:
    if d==1:
        if p<=x1<x2:
            tr+=(x2-p)*t1
            break
        else:
            tr+=(s-p)*t1
            p=s
            d=-1
    else:
        if x2<x1<=p:
            tr+=(p-x2)*t1
            break
        else:
            tr+=p*t1
            p=0
            d=1
print(min(tr,ig))
