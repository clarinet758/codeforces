#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.141592653589
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
#start = time.clock()
k=int(raw_input())
q=raw_input()
ans=[]
chk=''
t=set()
for i in q:
    if chk=='':
        chk=i
        t.add(i)
    elif len(t)<k and i not in t:
        ans.append(chk)
        chk=i
        t.add(i)
    else:
        chk+=i
ans.append(chk)
if len(ans)==k:
    print 'YES'
    for i in ans:
        print i
else:
    print 'NO'

        


#end = time.clock()
#print end - start
