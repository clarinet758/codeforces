#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys, io
import re, math
n,k=[int(x) for x in raw_input().split()]
l=[int(x) for x in raw_input().split()]
d={i:0 for i in range(1,k+1)}
for i in l:
    d[i]+=1
ans=0
while d[k]!=n:
    ans+=1
    for i in range(k-1,0,-1):
        if d[i]>0:
            d[i]-=1
            d[i+1]+=1
print ans
