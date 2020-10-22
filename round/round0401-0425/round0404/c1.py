#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,m=map(int,input().split())

if n<=m:
    print(n)
else:
    w=[1,10**19]
    for i in range(100):
        x=w[0]+w[1]
        x=x//2
        y=x+m

        p=x*m+n-m
        q=(y*(y+1)//2)-(m*(m+1)//2)
        if p>=q: w[0]=x
        else: w[1]=x
    x=w[0]
    y=x+m

    p=x*m+n-m
    q=(y*(y+1)//2)-(m*(m+1)//2)
    if p<=q: print(m+w[0])
    else: print(m+w[1])
    
    
    
    

"""
if n<=m:
    ans=m
    while 1:
        x-=ans
        if x<=0: break
        x=min(x+m,n)
        ans+=1
    print(ans)
else:
    ans=n-m
    w=[1,10**18]
    for i in range(100):
        p=w[0]+w[1]
        q=p*(p+1)//2
        if q<=ans:
            w[0]=p//2
        else:
            w[1]=p//2
    print(w)
    if w[0]*(w[0]+1)//2>=ans:
        print(ans+w[0])
    else:
        print(ans+w[1])
"""
