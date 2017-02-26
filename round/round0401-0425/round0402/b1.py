#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

t=cnt=0
n,k=input().split()
if len(n)<=int(k):
    print(len(n)-1)
else:
    k=int(k)
    for a,i in enumerate(n[::-1]):
        if i!='0':
            t+=1
        else:
            cnt+=1
        if cnt==k:
            break
    print(t if t!=len(n)-n.count('0') else len(n)-1)
# 1100 2


