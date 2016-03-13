#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
import collections
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.141592653589
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

#n=int(raw_input())
#n,k=map(int,raw_input().split())
#l=map(int,raw_input().split())
ans=chk=0
#end = time.clock()
#print end - start

class UnionFind:
    def __init__(self,size):
        self.rank=[0]*size
        self.par=range(size)
        self.g_num=size

    def find(self, x):
        if x==self.par[x]:
            return x
        self.par[x]=self.find(self.par[x])
        return self.par[x]

    def same(self,x,y):
        return self.find(x)==self.find(y)

    def unite(self,x,y):
        x,y=self.find(x),self.find(y)
        if x==y:
            return
        self.g_num-=1
        if self.rank[x]>self.rank[y]:
            self.par[y]=x
        else:
            self.par[x]=y
            if self.rank[x]==self.rank[y]:
                self.rank[y]+=1

    def group_num(self):
        return self.g_num

def sol(i,uni):
    #print i,uni
    tansaku=uni[i[0]]+uni[i[1]]
    tmp=set([x for x in tansaku if tansaku.count(x)>1])
    if len(tmp)==0:
        return 0
    kaeshi=-1
    for j in tmp:
        if kaeshi==-1:
            kaeshi=len(uni[i[0]])+len(uni[i[1]])+len(uni[j])-6
        else:
            kaeshi=min(kaeshi,len(uni[i[0]])+len(uni[i[1]])+len(uni[j])-6)
    return kaeshi
    
N,Q=map(int,raw_input().split())
l=[]
uni={}
hen=[0]*N
t=range(N)
for i in range(Q):
    a,b=map(int,raw_input().split())
    l.append((min(a-1,b-1),max(a-1,b-1)))
    hen[a-1]+=1
    hen[b-1]+=1
    if uni.has_key(a-1):
        uni[a-1].append(b-1)
    else:
        uni[a-1]=[b-1]
    if uni.has_key(b-1):
        uni[b-1].append(a-1)
    else:
        uni[b-1]=[a-1]
ans-=1
l.sort()
print l,uni
exit()
for i in l:
    m=sol(i,uni)
    if m!=0:
        ans=min(ans,m)
print ans
exit()

for i in range(0,Q-2):
    for j in range(i+1,Q-1):
        if l[i][0]!=l[j][0] and l[i][0]!=l[j][1]:
            continue
        elif l[i][1]<l[j][0]:
            break
        for k in range(j+1,Q):
            if l[i][1]<l[k][0]:
                break
            tmp=list(set([l[i][0],l[i][1],l[j][0],l[j][1],l[k][0],l[k][1]]))
            if len(tmp)==3 and ans==-1:
                ans=hen[tmp[0]]+hen[tmp[1]]+hen[tmp[2]]-6
            elif len(tmp)==3:
                ans=min(ans,hen[tmp[0]]+hen[tmp[1]]+hen[tmp[2]]-6)
print ans
exit()


memo=[0]*N
uf=UnionFind(N)
for loop in xrange(Q):
    a,b=map(int,raw_input().split())
    uf.unite(a-1,b-1)
    hen[a-1]+=1
    memo[a-1]+=1

chk=[0]*N
for i in range(N):
    for j in range(N):
        if uf.same(i,j):
            chk[i]+=1

for i in range(N-1,-1,-1):
    for j in range(N):
        if i!=j and uf.same(i,j):
            hen[j]+=memo[i]
            memo[i]=0
ans=-1
for i in range(N):
    if hen[i]==chk[i] and chk[i]>=3 and ans==-1:
        ans=chk[i]
    elif hen[i]==chk[i] and chk[i]>=3:
        ans=min(ans,chk[i])
    
