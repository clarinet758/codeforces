#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n,k=map(int,raw_input().split())
s=raw_input()
if s.index('T')<s.index('G'):
    s=s[::-1]
s+='..'*k

cnt=s.index('G')
while cnt<=n:
    if s[cnt+k]=='T':
        print 'YES'
        exit()
    elif s[cnt+k]=='#':
        break
    elif s[cnt+k]=='.':
        cnt+=k
print 'NO'

