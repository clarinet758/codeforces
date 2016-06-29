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
def calc_exp(n, p):
    e = 0
    while n % p == 0:
        e += 1
        n /= p
    return e, n

def gen_prime_candidates():
    yield 2
    n = 3
    while True:
        yield n
        n += 2

def factorize(n):
    f = ()
    for m in gen_prime_candidates():
        if m * m > n:
            break
        e, n = calc_exp(n, m)
        if e:
            f = f + ( (m, e), )
    if n != 1:
        f = f + ( (n, 1), )
    return f

def gen_divisors(f, k = 0):
    if k == len(f):
        yield 1
    else:
        p, e = f[k]
        for d in gen_divisors(f, k + 1):
            for e1 in range(e + 1):
                yield p ** e1 * d


n=int(raw_input())
f = factorize(n)
l=[]
tmp=[]
for d in gen_divisors(f):
    l.append(d)
l.sort()
t=len(l)
tmp=l[:]
for j in l:
    if j>1:
        while tmp[-1]%(j**2)==0:
            tmp.pop(-1)
    elif j**2>tmp[-1] or j not in tmp:
        break
print tmp[-1]
#n,k=map(int,raw_input().split())
#l=map(int,raw_input().split())
ans=chk=0

#end = time.clock()
#print end - start
