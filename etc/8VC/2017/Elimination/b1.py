#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n,m=map(int,input().split())
a=set([input() for i in range(n)])
b=set([input() for i in range(m)])
chk=a&b
a-=chk
b-=chk
for i in range(n+m+1):
    if len(chk):
        chk.pop()
    elif i%2==0 and len(a):
        a.pop()
    elif i%2 and len(b):
        b.pop()
    else:
        print('YES' if i%2 else 'NO')
        break


