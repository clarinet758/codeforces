#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

t=int(input())
for i in range(t):
    ans=[]
    n=int(input())
    for a in range(1,10):
        if n==a:
            ans.append(a)
        for b in range(a+1,10):
            if n==a+b:
                ans.append(a*10+b)
            for c in range(b+1,10):
                if n==a+b+c:
                    ans.append(a*100+b*10+c)
                for d in range(c+1,10):
                    if n==a+b+c+d:
                        ans.append(a*1000+b*100+c*10+d)
                    for e in range(d+1,10):
                        if n==a+b+c+d+e:
                            ans.append(a*10000+b*1000+c*100+d*10+e)
                        for f in range(e+1,10):
                            if n==a+b+c+d+e+f:
                                ans.append(a*100000+b*10000+c*1000+d*100+e*10+f)
                            for g in range(f+1,10):
                                if n==a+b+c+d+e+f+g:
                                    ans.append(a*1000000+b*100000+c*10000+d*1000+e*100+f*10+g)
                                for h in range(g+1,10):
                                    if n==a+b+c+d+e+f+g+h:
                                        ans.append(a*10000000+b*1000000+c*100000+d*10000+e*1000+f*100+g*10+h)
                                    for i in range(h+1,10):
                                        if n==a+b+c+d+e+f+g+h+i:
                                            ans.append(a*100000000+b*10000000+c*1000000+d*100000+e*10000+f*1000+g*100+h*10+i)
    if len(ans)>1: ans.sort()
    print(ans[0] if len(ans)>0 else -1)
            
