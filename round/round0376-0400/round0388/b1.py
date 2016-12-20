#!/usr/bin/env python
# -*- coding: UTF-8 -*-

xa,ya=[int(i) for i in raw_input().split()]
xb,yb=[int(i) for i in raw_input().split()]
xc,yc=[int(i) for i in raw_input().split()]
a=xb-xa
b=yb-ya
c=xc-xa
d=yc-ya
tmp=abs(a*d-b*c)
if tmp==0:
    print 0
    exit()
print 3
print xa+xb-xc,ya+yb-yc
print xa+xc-xb,ya+yc-yb
print xc+xb-xa,yc+yb-ya


