#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n=int(input())
s='bbaa'*((n+4)//4)
s=s[:n]
print(s)
