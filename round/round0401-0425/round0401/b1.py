#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

def gen(s):
    a={}
    for i in s:
        i=int(i)
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    return a

n=int(input())
a=input()
b=input()
ans=[n,0]
M,M2=gen(b),gen(b)


for i in a:
    i=int(i)
    f=[0,0]
    for j in range(i,10):
        if j in M and M[j]>0 and f[0]==0:
            M[j]-=1
            ans[0]-=1
            f[0]=1
        if j+1 in M2 and M2[j+1]>0 and f[1]==0:
            M2[j+1]-=1
            ans[1]+=1
            f[1]=1
        if sum(f)==2:
            break
print(ans[0],ans[1],sep='\n')



