#!/usr/bin/env python
# -*- coding: UTF-8 -*-

xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]

s=raw_input()
p=ord(s[0])-ord('a')+1
q=int(s[1])
ans=0
for x,y in xy+bs:
    if 0<p+x<9 and 0<q+y<9:
        ans+=1
print ans
