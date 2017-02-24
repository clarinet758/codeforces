#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-
"""
0 1 2 2 1 0 
1 0 0 1 2 2 
2 2 1 0 0 1 
"""
n=int(input())%6
x=int(input())
ans=[(0,1,2),(1,0,2),(2,0,1),(2,1,0),(1,2,0),(0,2,1)]
print(ans[n].index(x))
