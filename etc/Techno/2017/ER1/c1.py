#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys

n=int(raw_input())
l=[]
ans=[0]*n
for i in range(n):
    if i!=n-1:
        print '?',i+1,i+2
        sys.stdout.flush()
    else:
        print '?','1','3'
        sys.stdout.flush()
    l.append(int(raw_input()))
ans[0]=l[0]-(l[0]+l[1]-l[-1])/2
for i in range(1,n):
    ans[i]=l[i-1]-ans[i-1]
print '!',' '.join(map(str,ans))
