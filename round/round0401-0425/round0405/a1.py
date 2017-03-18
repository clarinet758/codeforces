#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

a,b=map(int,input().split())
ans=chk=0
while a<=b:
    a*=3
    b*=2
    ans+=1
print(ans)
