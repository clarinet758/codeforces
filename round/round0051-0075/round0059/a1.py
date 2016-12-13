#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys, io
import re, math
#start = time.clock()
n=int(raw_input())
d={'captain':[],'man':[],'woman':[],'child':[],'rat':[]}
for i in range(n):
    a,b=[x for x in raw_input().split()]
    if b=='woman': b='child'
    d[b].append(a)
for i in ['rat','child','man','captain']:
    for j in d[i]:
        print j
