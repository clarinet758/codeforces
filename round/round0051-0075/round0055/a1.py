#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys, io
import re, math
#start = time.clock()
up=low=0
j=''
n=raw_input()
for i in n:
    if i.isupper():
        up+=1
    else:
        low+=1
if low>=up:
    for k in n:
        j+=k.lower()
else:
    for k in n:
        j+=k.upper()
print j



#end = time.clock()
#print end - start
