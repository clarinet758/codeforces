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
#start = time.clock()
## WA!!
n=int(raw_input())
l=[int(x) for x in raw_input().split()]
t=l.index(min(l))
tmp=l[t:]+l[:t]
for a,i in enumerate(sorted(l)):
    if tmp[a]!=i:
        print -1
        exit()
print n-t if t!=0 else 0
