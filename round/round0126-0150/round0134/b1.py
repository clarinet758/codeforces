#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-
import sys
import re
import math
import itertools
import collections
import bisect
import heapq

def sol(tmp,x,y):
    s=[0,0]
    while tmp:
        tmp-=1
        t=heapq.heappop(x)
        u=y.pop()
        s[0]+=t
        s[1]+=u
        t-=1
        u-=1
        y.append(u)
        y.sort()
        if t: heapq.heappush(x,t)
    return s


n,m=map(int,input().split())
a=[]
l=[heapq.heappush(a,int(i))  for i in input().split()]
b=a[:]
b.sort()
ans=sol(n,a,b)
print(ans[1],ans[0])
