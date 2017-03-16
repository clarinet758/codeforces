#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

# 途中

def cal(x):
    return (1+x)*(x//2)+[0,(x+1)//2][x%2==1]
n,m=map(int,input().split())
#chk=[[1,1500000000],[1,1125000000750000000]]
chk=[[1,1500000000],[1,1125000000750000000]]
while 1:
    tmp1=sum(chk[0])
    tmp2=cal(tmp1)


