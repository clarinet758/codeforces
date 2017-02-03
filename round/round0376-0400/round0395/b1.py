#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

from collections import deque

n=int(input())
a=[int(i) for i in input().split()]
chk=deque()
if n%4==0:
    for i in range(n//2):
        if i==0:
            chk.append(n//2-1)
            chk.append(n//2)
        elif i%2==1:
            chk.appendleft(chk[-1]+1)
            chk.append(chk[1]-1)
        else:
            chk.appendleft(chk[-1]-1)
            chk.append(chk[1]+1)
elif n%4==2:
    for i in range(n//2):
        if i==0:
            chk.append(n//2)
            chk.append(n//2-1)
        elif i%2==1:
            chk.appendleft(chk[-1]-1)
            chk.append(chk[1]+1)
        else:
            chk.appendleft(chk[-1]+1)
            chk.append(chk[1]-1)
elif n%4==3:
    chk.append(n//2)
    for i in range(n//2):
        if i%2==1:
            chk.append(chk[0]+1)
            chk.appendleft(chk[-2]-1)
        else:
            chk.append(chk[0]-1)
            chk.appendleft(chk[-2]+1)
else:
    chk.append(n//2)
    for i in range(n//2):
        if i%2==1:
            chk.append(chk[0]-1)
            chk.appendleft(chk[-2]+1)
        else:
            chk.append(chk[0]+1)
            chk.appendleft(chk[-2]-1)

ans=[a[i] for i in chk]
print(*ans)
