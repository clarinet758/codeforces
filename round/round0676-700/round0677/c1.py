#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

t=int(input())
for i in range(t):
    n=int(input())
    l=[int(i) for i in input().split()]
    for j in range(n):
        f=1
        p=l[j]
        if j==0:
            for k in range(1,n):
                if p>l[k]:
                    p+=1
                else:
                    f=0
                    break
        elif j==n-1:
            for k in range(n-2,-1,-1):
                if p>l[k]:
                    p+=1
                else:
                    f=0
                    break
        else:
            x=y=j
            while x>0 or y<n-1:
                if x>0 and l[x-1]<p:
                    x-=1
                    p+=1
                elif y<n-1 and l[y+1]<p:
                    y+=1
                    p+=1
                else:
                    f=0
                    break
        if f==1:
            print(j+1)
            break
        if f==0 and j==n-1:
            print(-1)

