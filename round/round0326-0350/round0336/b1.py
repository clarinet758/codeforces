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
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

## TLE
a=raw_input()
b=raw_input()
la,lb=len(a),len(b)
ans=chk=0
t=lb-la
for i in range(lb):
    tmp=max(0,i-t)
    tmp2=min(tmp+t+1,i+1)
    if b[i]=='0':
        ans+=a[tmp:tmp2].count('1')
    else:
        ans+=a[tmp:tmp2].count('0')
print ans

exit()
#end = time.clock()
#print end - start
