#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n,k,a,b=[int(i) for i in input().split()]
t=abs(a-b)
chk=max(1,k-1)
ans=''

if a==b:
    ans='BG'*((n+1)//2)
elif a>b:
    ans+=('G'*k+'B')*(t//chk)
    ans+='G'*max(1,(t%chk))+'B'
    ans+='GB'*(n//2)
else:
    ans+=('B'*k+'G')*(t//chk)
    ans+='B'*max(1,(t%chk))+'G'
    ans+='BG'*(n//2)
ans=ans[:n]
print(ans if ans.count('G')==a else 'NO')
