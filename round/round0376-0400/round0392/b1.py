#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

s=input()
d={i:'' for i in range(4)}
ans=[0]*4
for a,i in enumerate(s):
    if i!='!':
        d[a%4]=i
for a,i in enumerate(s):
    if i=='!':
        if d[a%4]=='R':
            ans[0]+=1
        elif d[a%4]=='B':
            ans[1]+=1
        elif d[a%4]=='Y':
            ans[2]+=1
        else:
            ans[3]+=1
print(*ans)
