#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Pypy2

n,m=map(int,raw_input().split())
l,r=[],[]
ans=0
for i in range(n):
    a=map(str,raw_input().split())
    tmp=''.join(a)
    l.append(tmp)
    chk=tmp.split('1')
    f=len(chk)
    if f==2:
        ans+=len(chk[0])+len(chk[1])
    elif f>2:
        for j in range(f):
            if j==0 or j==f-1:
                ans+=len(chk[j])
            elif j<f-1:
                ans+=len(chk[j])*2
for i in range(m):
    tmp=''
    for j in range(n):
        tmp=l[j][i]+tmp
    r.append(tmp)
for i in r:
    chk=i.split('1')
    f=len(chk)
    if f==2:
        ans+=len(chk[0])+len(chk[1])
    elif f>2:
        for j in range(f):
            if j==0 or j==f-1:
                ans+=len(chk[j])
            elif j<f-1:
                ans+=len(chk[j])*2
print ans
