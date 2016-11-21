#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
a=set(map(int,raw_input().split()))
ans=chk=0
if len(a)>3:
    print 'NO'
elif len(a)==3:
    tmp=max(a)-min(a)
    if tmp%2==0 and max(a)-tmp/2 in a and min(a)+tmp/2 in a:
        print 'YES'
    else:
        print 'NO'
elif len(a)<=2:
    print 'YES'
