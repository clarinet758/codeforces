#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-
import sys
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
pi=3.1415926535897932
IS=float('inf')
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
def niten(a,b): return abs(a-b) if a>=0 and b>=0 else  a+abs(b) if a>=0 else abs(a)+b if b>=0 else abs(abs(a)-abs(b))
def fib(n): return [(seq.append(seq[i-2] + seq[i-1]), seq[i-2])[1] for seq in [[0, 1]] for i in range(2, n)]
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def eucl(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0
def pscl(num,l=[1]):
    for i in range(num):
        l = map(lambda x,y:x+y,[0]+l,l+[0])
    return l

l=[]
for i in range(4):
    x=input()
    if 'xx.' in x or '.xx' in x or 'x.x' in x:
        print('YES')
        exit()
    elif 'ooo' in x:
        print('NO')
        exit()

    l.append(x)
for i in range(2):
    for j in range(4):
        tate=l[i][j]+l[i+1][j]+l[i+2][j]
        if 'xx.' in tate or '.xx' in tate or 'x.x' in tate:
            print('YES')
            exit()
        elif 'ooo' in tate:
            print('NO')
            exit()
        if j>=2:
            y=l[i][j]+l[i+1][j-1]+l[i+2][j-2]
            if 'xx.' in y or '.xx' in y or 'x.x' in y:
                print('YES')
                exit()
            elif 'ooo' in y:
                print('NO')
                exit()
        if j<2:
            y=l[i][j]+l[i+1][j+1]+l[i+2][j+2]
            if 'xx.' in y or '.xx' in y or 'x.x' in y:
                print('YES')
                exit()
            elif 'ooo' in y:
                print('NO')
                exit()
print('NO')
