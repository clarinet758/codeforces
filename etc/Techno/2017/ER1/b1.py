#!/usr/bin/env python
# -*- coding: UTF-8 -*-

d=c=0
s=raw_input()+'$'
tmp=''
for i in s:
    if i.isdigit() or i=='.':
        tmp+=i
    elif len(tmp):
        if len(tmp)<=2:
            d+=int(tmp)
        elif tmp[-3]=='.':
            c+=int(tmp[-2:])
            d+=int(tmp[:-2].replace('.',''))
        else:
            d+=int(tmp.replace('.',''))
        tmp=''
d+=c/100
c%=100
ans=''
if d==0:
    ans='0.'
else:
    while d:
        if d>=1000:
            tmp='{0:03d}'.format(d%1000)
            ans=tmp+'.'+ans
        else:
            ans=str(d)+'.'+ans
        d/=1000
if c:
    print ans+'{0:02d}'.format(c)
else:
    print ans.lstrip('0').rstrip('.')
