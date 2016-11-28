#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n,n1,n2=map(int,raw_input().split())
a=map(int,raw_input().split())
a.sort()
x=y=0
for i in range(min(n1,n2)):
    x+=a.pop()
for i in range(max(n1,n2)):
    y+=a.pop()
print x*1.0/min(n1,n2)+y*1.0/max(n1,n2)
