#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys, io
import re, math
start = time.clock()
i=raw_input()
l=[['*']*200 for a in range(200)]
x=y=100
chk=1
l[y][x]='#'
for j in range(len(i)):
    if i[j]=='U':
        l[y][x-1]=l[y][x+1]='#'
        y-=1
        if l[y][x]!='#':
            l[y][x]='#'
        else:
            chk=False
            break
    elif i[j]=='D':
        l[y][x-1]=l[y][x+1]='#'
        y+=1
        if l[y][x]!='#':
            l[y][x]='#'
        else:
            chk=False
            break
        
    elif i[j]=='R':
        l[y+1][x]=l[y-1][x]='#'
        x+=1
        if l[y][x]!='#':
            l[y][x]='#'
        else:
            chk=False
            break
    elif i[j]=='L':
        l[y+1][x]=l[y-1][x]='#'
        x-=1
        if l[y][x]!='#':
            l[y][x]='#'
        else:
            chk=False
            break
print 'OK' if chk else 'BUG'


end = time.clock()
print end - start
