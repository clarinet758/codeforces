#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
import collections
import bisect
import heapq

n=int(raw_input())
l=[]
ans=[]
for i in xrange(n):
    q=raw_input()
    if q[0]=='r' and len(l)==0:
        ans.append('insert 1')
        ans.append(q)
    elif q[0]=='r':
        heapq.heappop(l)
        ans.append(q)
    elif q[0]=='i':
        ans.append(q)
        t=int(q.replace('insert ',''))
        heapq.heappush(l,t)
    else:
        t=int(q.split()[1])
        if t not in l:
            ans.append('insert '+str(t))
            heapq.heappush(l,t)
        while l[0]!=t:
            ans.append('removeMin')
            heapq.heappop(l)
        ans.append('getMin '+str(t))
print len(ans)
#print '\n'.join(ans)
sys.stdout.write('\n'.join(ans))
#for i in ans:
#    print i


#end = time.clock()
#print end - start
