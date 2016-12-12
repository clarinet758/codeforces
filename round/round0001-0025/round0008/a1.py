#!/usr/bin/env python
# -*- coding: UTF-8 -*-

s=raw_input()
a=raw_input()
b=raw_input()
s1=len(s)
a1=len(a)
ans=[0,0]
for i in range(s1):
    x=s[i:i+a1]
    if s[i:i+a1]==a:
        if b in s[i+a1:]:
            ans[1]=1
    if a[::-1]==x:
        tmp=s[:i]
        if b[::-1] in tmp:
            ans[0]=1
print 'both' if sum(ans)==2 else 'forward' if ans[1]==1 else 'backward' if ans[0]==1 else 'fantasy'
