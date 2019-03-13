#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
input()
x=[int(i) for i in input().split()]
d=set()
ans=0
for i in x:
    if i in d:
        d.remove(i)
    else:
        d.add(i)
        ans=max(ans,len(d))
print(ans)
