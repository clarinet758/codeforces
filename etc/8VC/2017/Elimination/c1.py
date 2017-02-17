#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

input()
l=[int(i) for i in input().split()]
ans=0
w=set([])
for a,i in enumerate(l):
    if a+1==i:
        ans+=1
    else:
        w.add(i)
print(ans+len(w)//2)

