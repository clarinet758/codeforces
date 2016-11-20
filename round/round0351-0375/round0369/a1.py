#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
l=[]
ans=chk=0
for i in range(n):
    s=raw_input()
    if s[:2]=='OO' and chk==0:
        chk=1
        s='++'+s[2:]
    elif s[3:]=='OO' and chk==0:
        chk=1
        s=s[:3]+'++'
    l.append(s)
if chk:
    print 'YES'
    for i in l:
        print i
else:
    print 'NO'
