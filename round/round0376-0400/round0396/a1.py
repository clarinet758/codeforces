#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

a=input()
b=input()
print(max(len(a),len(b)) if a!=b else -1)
