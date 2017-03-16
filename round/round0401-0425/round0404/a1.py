#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

d={'Cube':6,'Tetrahedron':4,'Octahedron':8,'Dodecahedron':12, 'Icosahedron':20}
n=int(input())
ans=chk=0
for i in range(n):
    s=input()
    ans=ans+d[s]
print(ans)
