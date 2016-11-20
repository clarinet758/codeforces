#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def ed(x):
    print x
    exit()
n=int(raw_input())
if n==1:
    ed(n)
l=[]
ans=-1
chk=f=0
for i in range(n):
    tmp=map(int,raw_input().split())
    if i==0 and 0 in tmp:
        f=1
    elif i==1 and f==1:
        t0,t1=sum(l[0]),sum(tmp)
        ans=t1-t0
        if ans<1:
            ed(-1)
        l[0][l[0].index(0)]=ans
        chk=t1
    elif i==0:
        chk=sum(tmp)
    elif (0 in tmp or sum(tmp)!=chk) and f==1:
        ed(-1)
    elif 0 in tmp and f==0:
        ans=chk-sum(tmp)
        if ans<1:
            ed(-1)
        tmp[tmp.index(0)]=ans
        f=1
    l.append(tmp)

for i in range(n):
    y=0
    for j in range(n):
        y+=l[j][i]
    if y!=chk:
        ed(-1)
x1=x2=0
for i in range(n):
    x1+=l[i][i]
    x2+=l[i][-1*i-1]
if x1!=chk or x2!=chk:
    ed(-1)
print ans
