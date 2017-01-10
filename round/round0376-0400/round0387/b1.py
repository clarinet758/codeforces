#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n=int(input())
s=input()
ans=''
chk=[0]*4
for i in s:
    if i=='A':
        chk[0]+=1
    elif i=='C':
        chk[1]+=1
    elif i=='G':
        chk[2]+=1
    elif i=='T':
        chk[3]+=1
for i in s:
    if i!='?':
        ans+=i
    else:
        if min(chk)==chk[0]:
            ans+='A'
            chk[0]+=1
        elif min(chk)==chk[1]:
            ans+='C'
            chk[1]+=1
        elif min(chk)==chk[2]:
            ans+='G'
            chk[2]+=1
        else:
            ans+='T'
            chk[3]+=1
print(ans if len(set(chk))==1 else '===')
