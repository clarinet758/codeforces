#!/usr/bin/env python
# -*- coding: UTF-8 -*-

p={'b':'d','d':'b','p':'q','q':'p'}
c=['A','H','I','M','O','o','T','U','V','v','W','w','X','x','Y']
s=raw_input()
if len(s)%2==1:
    if s[len(s)/2] not in c:
        print 'NIE'
        exit()
for i in range(len(s)):
    if s[i] in c and s[-1*i-1]==s[i]:
        pass
    elif s[i] in p and p[s[i]]==s[-1*i-1]:
        pass
    else:
        print 'NIE'
        exit()
print 'TAK'


