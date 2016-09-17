#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
import collections
import bisect
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.141592653589
IS=float('inf')
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
def niten(a,b): return abs(a-b) if a>=0 and b>=0 else  a+abs(b) if a>=0 else abs(a)+b if b>=0 else abs(abs(a)-abs(b))
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

s=raw_input()
#n,k=map(int,raw_input().split())
#l=map(int,raw_input().split())
w=[0]*26
ans=chk=q=f=0
memo='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for a,i in enumerate(s):
    if i!='?':
        w[ord(i)-65]+=1
    else:
        q+=1
    if a>=25:
        if w.count(1)+q==26:
            f=1
            ans=''
            tmp=0
            for j in s[a-25:a+1]:
                if j!='?':
                    ans+=j
                    memo=memo.replace(j,'')
                else:
                    ans+=chr(tmp+97)
                    tmp+=1
            o=97
            for j in ans:
                if not j.isupper():
                    ans=ans.replace(chr(o),memo[0])
                    memo=memo[1:]
                    o+=1
            #print s[:a-25]+ans+s[a+1:]
            s=s[:a-25]+ans+s[a+1:]
            w=[0]*26
            q=0
            memo='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if s[a-25]!='?':
            w[ord(s[a-25])-65]-=1
        else:
            q-=1
s=s.replace('?','A')
print -1 if f==0 else s
#end = time.clock()
#print end - start
