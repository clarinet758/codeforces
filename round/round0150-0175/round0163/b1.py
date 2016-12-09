#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#start = time.clock()
n,t=map(int,raw_input().split())
l=list(raw_input())
f=0
for i in range(t):
    for j in range(n-1,0,-1):
        if l[j]=='G' and l[j-1]=='B' and f==0:
            l[j],l[j-1]=l[j-1],l[j]
            f=1
        else:
            f=0
print ''.join(l)
