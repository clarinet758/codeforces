#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

def prime_t(t):
    i=2
    while i**2<=t:
        if t%i==0:
            return 0
        i+=1
    return 1

l=[]
for i in range(2,10000):
    if prime_t(i):
        l.append(i)

n=int(input())
for i in range(1,1001):
    if (n*i+1) not in l:
        print(i)
        exit()

