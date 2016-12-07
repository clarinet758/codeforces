#!/usr/bin/env python
# -*- coding: UTF-8 -*-
s=raw_input()
l=0
ans1=''
ans2=''
for i in s:
    if i.islower():
        l+=1
    ans1+=i.lower()
    ans2+=i.upper()

if l*2>=len(s):
    print ans1
else:
    print ans2

