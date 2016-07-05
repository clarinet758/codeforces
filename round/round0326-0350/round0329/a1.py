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
n=int(raw_input())
l=[]
ans=0
for i in range(n):
    w=list(raw_input())
    if len(set(w))<3:
        w.sort()
        l.append(w)
for i in range(26):
    for j in range(i,26):
        tmp=0
        x,y=chr(i+97),chr(j+97)
        for k in l:
            if x==y:
                if k[0]==k[-1]==x:
                    tmp+=len(k)
            else:
                chk=[x,y]
                if k[0] in chk and k[-1] in chk:
                    tmp+=len(k)
        ans=max(ans,tmp)
print ans

#n,k=map(int,raw_input().split())
#l=map(int,raw_input().split())
#end = time.clock()
#print end - start
