#!/usr/bin/env python

n,k=map(int, raw_input().split())
if k<=(n+1)/2:
    print 1+(k-1)*2
else:
    print (k-(n+1)/2)*2

