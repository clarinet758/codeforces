#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
x=ord("a")
ans=""
for i in range(n):
    ans+=chr(x+i%k)
print(ans)
