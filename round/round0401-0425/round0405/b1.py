#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

n,m=map(int,raw_input().split())

e=[0]*n
t=[1]*n

r=[0]*n
p=[int(i) for i in range(n)]


def find(a):
    if a==p[a]:
        return a

#新しい親になる頂点を決めて辺や頂点の数をまとめる
    tmp=find(p[a])
    t[tmp]=t[tmp]+t[a]
    t[a]=0
    e[tmp]=e[tmp]+e[a]
    e[a]=0

    p[a]=tmp
    return p[a]

def unite(a,b):
    a,b=find(a),find(b)
    if a==b:
        return

    if r[a]<r[b]:
        p[a]=b
    else:
        p[b]=a
        if r[a]==r[b]:
            r[a]=r[a]+1
    k=p[a]
    if k!=a:
        t[k]=t[k]+t[a]
        t[a]=0
        e[k]=e[k]+e[a]
        e[a]=0
    if k!=b:
        t[k]=t[k]+t[b]
        t[b]=0
        e[k]=e[k]+e[b]
        e[b]=0


for i in range(m):
    a,b=map(int,raw_input().split())
    a-=1
    b-=1
    e[a]=e[a]+1
    unite(a,b)

p=set(p)
ans=1
for i in p:
    if t[i]>1:
        k=t[i]
        if e[i]!=k*(k-1)//2:
            ans=0
            break

print(['NO','YES'][ans])
