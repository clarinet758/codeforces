#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
l=map(int,raw_input().split())

if l[-1]==15 or (n>1 and l[-1]!=0 and l[-2]-l[-1]>0):
    print 'DOWN'
elif l[-1]==0 or (n>1 and l[-2]-l[-1]<0):
    print 'UP'
else:
    print -1
