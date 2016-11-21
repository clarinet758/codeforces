#!/usr/bin/env python
# -*- coding: UTF-8 -*-

l1,r1,l2,r2,k=map(int,raw_input().split())
s=max(l1,l2)
g=min(r1,r2)
print g-s if g>=s and s<=k<=g else g-s+1 if g>=s else 0
