#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-
import bisect

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


n=int(input())
l=[int(i) for i in input().split()]
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
l=list(set(l))
l.sort()

chk=prime_list(max(l))
ans=[0]*(len(chk)+1)
for i in l:
    tmp=i
    for j,k in enumerate(chk):
        if i%k==0:
            ans[j]+=d[tmp]
            while i%k==0:
                i//=k
        if i<k:
            break
print(max(max(ans),1))
