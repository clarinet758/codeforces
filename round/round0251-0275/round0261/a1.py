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
x1,y1,x2,y2=map(int,raw_input().split())
if x1==x2:
    chk=abs(y2-y1)
    print x1+chk,y1,x2+chk,y2
elif y1==y2:
    chk=abs(x2-x1)
    print x1,y1+chk,x2,y2+chk
else:
    if abs(x2-y1)==abs(y2-x1):
        print x1,y2,x2,y1
    else:
        print -1
#end = time.clock()
#print end - start
