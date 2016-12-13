#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys, io
import re, math
#start = time.clock()
n=int(raw_input())
rat,child,man,cap=[],[],[],[]
for i in range(n):
    w=map(str, raw_input().split())
    if w[1]=='rat': rat.append(w[0])
    elif w[1]=='woman' or w[1]=='child': child.append(w[0])
    elif w[1]=='man': man.append(w[0])
    else: cap.append(w[0])
for i in rat:
    print i
for i in child:
    print i
for i in man:
    print i
for i in cap:
    print i
#l=[int(x) for x in raw_input().split()]
#end = time.clock()
#print end - start
