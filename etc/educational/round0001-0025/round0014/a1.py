#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
l=map(int,raw_input().split())
print 'YES' if (l.count(0)==1 and n!=1) or (n==1 and l[0]==1)  else 'NO'
