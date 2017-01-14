#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

def prime_t(t):
    i=2
    while i**2<=t:
        if t%i==0:
            return 0
        i+=1
    return 1
p=[]

for i in range(2,100001):
    if prime_t(i):
        p.append(i)

n=int(input())
ol=[int(i) for i in input().split()]
l=[i for i in ol if int(i)%2]
ans=max(1,n-len(l))

pd={i:0 for i in p}
for i in ol:
    if i in pd:
        pd[i]+=1
        ans=max(ans,pd[i])
l=[i for i in ol if i not in pd]


ld={}
for i in l:
    if i in ld:
        ld[i]+=1
    else:
        ld[i]=1
setl=set(l)
mol=list(setl)
mol.sort()

for i in mol:
    so=i
    for j in p:
        tmp=1
        if j/2>so:
            break
        elif so%j==0:
            pd[j]+=ld[i]
            while so%j==0:
                so//=j
            ans=max(ans,pd[j],tmp)
print(ans)
