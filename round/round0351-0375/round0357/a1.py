#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
ans=chk=0
for i in range(n):
    name,before,after=map(str,raw_input().split())
    if int(before)>=2400 and int(before)<int(after):
        print 'YES'
        exit()
print 'NO'
