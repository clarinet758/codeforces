#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

import heapq

n=int(input())
l=[int(i) for i in input().split()]
l=l[::-1]
st=[]
b=f=n
while f:
    tmp=l.pop()
    heapq.heappush(st,-tmp)
    if tmp==b:
        p,m=[],[]
        for i in range(len(st)):
            k=-1*(heapq.heappop(st))
            if i==0 or p[-1]-1==k:
                b-=1
                p.append(k)
            else:
                m.append(-k)
        print(*p)
        st=m
    else:
        print()
    f-=1


