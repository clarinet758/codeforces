#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n,m=map(int,input().split())
a=set([input() for i in range(n)])
b=set([input() for i in range(m)])
chk=a&b
a-=chk
b-=chk
print('YES' if (len(a)>len(b)-len(chk)%2) else 'NO')


