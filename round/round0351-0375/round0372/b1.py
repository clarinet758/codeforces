#!/usr/bin/env python
# -*- coding: UTF-8 -*-

s=raw_input()
l=set([chr(x+ord('A')) for x in range(26)])
for i in range(len(s)-25):
    ans=''
    t=s[i:i+26]
    if ('?' not in t and len(set(t))==26) or ('?' in t and len(set(t))+t.count('?')==27):
        ans+=s[:i]
        tmp=s[i:i+26]
        dif=l-set(tmp)
        for k in tmp:
            if k=='?':
                ans+=dif.pop()
            else:
                ans+=k
        ans+=s[i+26:]
        ans=ans.replace('?','A')
        print ans
        exit()
print -1
