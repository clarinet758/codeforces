#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n=int(input())
a=input()
b=input()
ans=[n,0]
M,M2={},{}
for i in b:
    i=int(i)
    if i in M:
        M[i]+=1
    else:
        M[i]=1
for i in b:
    i=int(i)
    if i in M2:
        M2[i]+=1
    else:
        M2[i]=1

for i in a:
    i=int(i)
    for j in range(i,10):
        if j in M and M[j]>0:
            M[j]-=1
            ans[0]-=1
            break

for i in a:
    i=int(i)
    for j in range(i+1,10):
        if j in M2 and M2[j]>0:
            M2[j]-=1
            ans[1]+=1
            break
print(ans[0])
print(ans[1])



