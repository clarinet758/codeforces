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
#TLE解決できず　しゃくとりは無理っぽい
n=int(raw_input())
#n,k=map(int,raw_input().split())
l=map(int,raw_input().split())
ans=1
i=0
memo=[l[0],0]
while i<n-1:
    cnt=1
    chk=-1
    if (n-1)-i<ans: break
    for j in range(i+1,n):
        #print memo
        if l[j-1]!=memo[0]:
            memo[0]=l[j-1]
            memo[1]=j-1
        if l[j-1]==l[j] or l[i]==l[j]:
            cnt+=1
        elif (abs(l[j-1]-l[j])==1 and chk==-1) or l[j]==chk:
            chk=l[j]
            cnt+=1
        else:
            break
    ans=max(ans,cnt)
    i=memo[1]
print ans

#end = time.clock()
#print end - start
