#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


n=input()
l=[int(i) for i in n]
ans=[sum(l),n]
for i in range(len(n)-1):
    t0=0
    t1=""
    for j in range(len(n)-1):
        if i==j:
            t0+=l[j]-1
            t1+=str(l[j]-1)
            t0+=9*(len(n)-j-1)
            t1+="9"*(len(n)-j-1)
            break
        else:
            t0+=l[j]
            t1+=str(l[j])
    if t0>=ans[0]:
        ans[0]=t0
        ans[1]=t1
if ans[0]==sum(l):
    ans[1]=n
print(int(ans[1]))
            
