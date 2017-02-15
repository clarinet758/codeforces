#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

def prime_t(t):
    i=2
    while i**2<=t:
        if t%i==0:
            return 0
        i+=1
    return 1

def prime_list(tt):
    p_list=[]
    for i in range(2,tt+1):
        if prime_t(i):
            p_list.append(i)
    return p_list


chk=prime_list(10001)
n=int(input())
for i in range(1,1000):
    if n*i+1 not in chk:
        print(i)
        break
