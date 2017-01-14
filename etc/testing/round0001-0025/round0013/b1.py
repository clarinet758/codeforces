#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

tmp='0000'
k=''
chk=set()
for a in '0123':
    for b in '0123':
        for c in '0123':
            for d in '0123':
                if len(set([a,b,c,d]))==4:
                    chk.add(a+b+c+d)
while 1:
    print(tmp, flush=True)
    a,b=[int(i) for i in input().split()]
    c=''
    if a==4 and b==0:
        break
    if len(k)<4:
        if a>0:
            k+=tmp[:a]
        tmp=str((int(tmp[0])+1)%10)*4
    else:
        p=chk.pop()
        tmp=k[int(p[0])]+k[int(p[1])]+k[int(p[2])]+k[int(p[3])]

