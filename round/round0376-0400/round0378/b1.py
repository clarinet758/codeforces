#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
a=[]
l=r=ans=chk=0
p,q=[0]*3,[0]*3
for i in range(n):
    x,y=map(int,raw_input().split())
    l,r=l+x,r+y
    if x>y:
        if x-y>p[0]-p[1]:
            p=[x,y,i+1]
    if x<y:
        if y-x>q[1]-q[0]:
            q=[x,y,i+1]
ll=abs((l-q[0]+q[1])-(r-q[1]+q[0]))
rr=abs((l-p[0]+p[1])-(r-p[1]+p[0]))
print 0 if abs(l-r)==max(abs(l-r),ll,rr) else q[2] if ll>rr else p[2]
