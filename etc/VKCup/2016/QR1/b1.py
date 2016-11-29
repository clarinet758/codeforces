#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
l=[raw_input() for i in range(n)]
chk=set()
while len(l):
    tmp=l.pop()
    if tmp not in chk:
        print tmp
        chk.add(tmp)
