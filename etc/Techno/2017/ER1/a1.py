#!/usr/bin/env python
# -*- coding: UTF-8 -*-

a,b=map(int,raw_input().split())
ans=[str(b)]
while 1:
    if b%10==1:
        ans.append(str(b/10))
        b/=10
    elif b%2==0:
        ans.append(str(b/2))
        b/=2
    else:
        print 'NO'
        break
    if b==a:
        print 'YES'
        print len(ans)
        print ' '.join(ans[::-1])
        break
    if b<a:
        print 'NO'
        break
