#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n,m,z=map(int,input().split())
a=set([int(i)*n for i in range(1,z+1) if int(i)*n<=z])
b=set([int(i)*m for i in range(1,z+1) if int(i)*m<=z])
print(len(a&b))
