#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
a,b,c=1234567,123456,1234
for i in range(811):
    tmp=n-a*i
    for j in range(tmp/b+1):
        if (tmp-b*j)%c==0:
            print 'YES'
            exit()
print 'NO'
