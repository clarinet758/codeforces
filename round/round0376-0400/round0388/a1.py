#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
if n==3:
    print 1
    print 3
elif n%2:
    print n/2
    for i in range(n/2-1):
        print 2,
    print 3
else:
    print n/2
    for i in range(n/2):
        print 2,
