#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
import collections
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.141592653589
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
#start = time.clock()
#n=int(raw_input())
a,b=map(int,raw_input().split())
#l=map(int,raw_input().split())
ans=chk=0
#if abs(a-b)<2:
print min(a,b),(max(a,b)-min(a,b))/2
#end = time.clock()
#print end - start
