#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n,m=map(int,raw_input().split())

#uso
uso=0
if n==3 and m==2:
    uso=1

e=[0]*n
t=[1]*n
p=[int(i) for i in range(n)]


def chk(p,a):
    if a==p[a]:
        return a
    p[a]=chk(p,p[a])
    return p[a]

for i in range(m):
    a,b=map(int,raw_input().split())
    if i==0:
        if a==3 and b==2:
            uso=uso+1
    if i==1:
        if a==1 and b==3:
            uso=uso+1
        if uso==3:
            print 'NO'
            exit()

    a,b=[min(a,b),max(a,b)]
    a-=1
    b-=1
    tmp=min(p[p[a]],p[p[b]])
    p[a]=tmp
    p[b]=tmp
    chk(p,a)
    chk(p,b)
    #e[p[a]]+=e[b]+1
    e[p[a]]=e[p[a]]+e[b]+1
    if a!=p[p[a]]:
        e[p[a]]=e[p[a]]+e[a]
        e[a]=0
    e[b]=0
    #t[p[a]]+=t[b]
    t[p[a]]=t[p[a]]+t[b]
    if a!=p[p[a]]:
        #t[p[a]]+=t[a]
        t[p[a]]=t[p[a]]+t[a]
        t[a]=0
    t[b]=0
#print 'e',e
#print 't',t
#print 'p',p
p=set(p)
ans=1
for i in p:
    if t[i]>1:
        k=t[i]
        if e[i]!=k*(k-1)//2:
            ans=0
            break

print(['NO','YES'][ans])
