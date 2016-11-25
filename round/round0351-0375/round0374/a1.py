#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n=int(raw_input())
ans=[str(len(x)) for x in map(str,raw_input().split('W')) if len(x)>0]
print len(ans)
print ' '.join(ans)
