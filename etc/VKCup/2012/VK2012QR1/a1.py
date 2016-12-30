#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#start = time.clock()
n,k=map(int,raw_input().split())
l=[int(x) for x in raw_input().split()]
ans=chk=0
for i in range(n):
    if l[i]>=l[k-1] and l[i]>0:
        ans+=1
print ans


#end = time.clock()
#print end - start
