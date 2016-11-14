#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
l=map(int,raw_input().split())

d={}
ans=chk=0
chk=sum(l)/(n/2)
for a,i in enumerate(l):
    if i in d:
        d[i].append(a+1)
    else:
        d[i]=[a+1]
while 1:
    if len(d)==0:
        break
    for i in d:
        print d[i].pop(),
        print d[chk-i].pop()
        if len(d[i])==0:
            del d[i]
        if len(d)>0 and len(d[chk-i])==0:
            del d[chk-i]
        break
