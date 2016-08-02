#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
import collections
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.141592653589
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
#start = time.clock()
#n=int(raw_input())
n,m=map(int,raw_input().split())
f=map(int,raw_input().split())
b=map(int,raw_input().split())
a=['0']*m
ans=chk=0
p=q=0
for x,i in enumerate(b):
    if p==0 and f.count(i)==1:
        a[i-1]=str(f.index(i)+1)
    elif f.count(i)>1:
        p=1
    else:
        print 'Impossible'
        exit()
if p==1 or a.count('0')>0:
    print 'Ambiguity'
else:
    print 'Possible'
    print ' '.join(a)

#end = time.clock()
#print end - start
