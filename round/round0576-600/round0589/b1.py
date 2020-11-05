#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

mod=1000000007
h,w=map(int,input().split())
x=[[2]*(w+1) for _ in range(h+1)]
r=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
for i in range(h):
    if r[i]==0:
        x[i][0]=0
    else:
        for j in range(r[i]):
            x[i][j]=1
        x[i][r[i]]=0
for i in range(w):
    if c[i]==0 and x[0][i]==1:
        print(0)
        exit()
    elif c[i]==0:
        x[0][i]=0
    else:
        for j in range(c[i]):
            if x[j][i]==0:
                print(0)
                exit()
            else:
                x[j][i]=1
        #if x[c[i]][i]=0
        if x[c[i]][i]==1:
            print(0)
            exit()
        else:
            x[c[i]][i]=0
ans=0 
for i in range(h):
    for j in range(w):
        ans+=(x[i][j]==2) 
print(pow(2,ans,mod))
