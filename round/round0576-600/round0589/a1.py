#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

l,r=map(int,input().split())
for i in range(l,r+1):
    if len(str(i))==len(set(list(str(i)))):
        print(i)
        exit()
print(-1)
