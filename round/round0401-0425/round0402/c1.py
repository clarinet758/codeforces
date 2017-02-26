#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
p=n
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
N=[i for i in range(n)]
ind=[0]*n
chk=set([])
d={}
ans=0
for i in N:
    tmp=a[i]-b[i]
    ind[i]=tmp
    if tmp in d:
        d[tmp].append(i)
    else:
        d[tmp]=[i]
        chk.add(tmp)
chk=list(chk)
chk.sort()
chk=chk[::-1]
for i in range(n):
    if i>=k and chk[-1]>0:
        break
    ans+=a[d[chk[-1]][-1]]
    d[chk[-1]].pop()
    p-=1
    if len(d[chk[-1]])==0:
        del d[chk[-1]]
        chk.pop()

for i in range(p):
    ans+=b[d[chk[-1]][-1]]
    d[chk[-1]].pop()
    if len(d[chk[-1]])==0:
        del d[chk[-1]]
        chk.pop()
print(ans)

