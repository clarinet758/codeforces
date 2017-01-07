#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n=int(input())
s=input()
ans=''
for a,i in enumerate(s):
    if (a+n)%2:
        ans+=i
    else:
        ans=i+ans
print(ans)
