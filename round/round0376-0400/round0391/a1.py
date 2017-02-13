#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-
w="Bulbasaur"
s=input()
ans=10**5+1
chk={}
for i in s:
    if i in chk:
        chk[i]+=1
    else:
        chk[i]=1
for i in w:
    if i in chk:
        ans=min(ans,chk[i]//[1,2][i=='a' or i=='u'])
    else:
        ans=0
print(ans)

