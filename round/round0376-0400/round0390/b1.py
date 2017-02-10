#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

l=[]
for i in range(4):
    l.append(input())
ans=0
a=b=c=d=''
for i in range(4):
    for j in range(4):
        if j<2:
            a=l[i][j]+l[i][j+1]+l[i][j+2]
        if i<2:
            b=l[i][j]+l[i+1][j]+l[i+2][j]
        if i<2 and j<2:
            c=l[i][j]+l[i+1][j+1]+l[i+2][j+2]
        if i<2 and j>1:
            d=l[i][j]+l[i+1][j-1]+l[i+2][j-2]
        for k in (a,b,c,d):
            if k.count('.')==1 and k.count('x')==2:
                ans=1
print('YES' if ans else 'NO')

            
