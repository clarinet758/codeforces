#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

a,b=map(int,input().split())
print('YES' if (a+b>0) and (a==b or a+1==b or a==b+1) else 'NO')
