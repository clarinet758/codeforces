#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

w=[]
n=int(input())
for i in range(1,10):
    for j in range(1,5):
        w.append(str(i)*j)

for i in range(n):
    s=input()
    cnt=0
    for k in w:
        cnt+=len(k)
        if s==k:
            print(cnt)
