#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

l=[]
ans=0
for i in range(4):
    x=input()
    if 'xx.' in x or '.xx' in x or 'x.x' in x:
        ans=1
    l.append(x)

for i in range(2):
    for j in range(4):
        tate=l[i][j]+l[i+1][j]+l[i+2][j]
        if 'xx.' in tate or '.xx' in tate or 'x.x' in tate:
            ans=1
        if j>=2:
            y=l[i][j]+l[i+1][j-1]+l[i+2][j-2]
            if 'xx.' in y or '.xx' in y or 'x.x' in y:
                ans=1
        if j<2:
            y=l[i][j]+l[i+1][j+1]+l[i+2][j+2]
            if 'xx.' in y or '.xx' in y or 'x.x' in y:
                ans=1
print('YES' if ans else 'NO')
