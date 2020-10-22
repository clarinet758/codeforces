#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

d={"Tetrahedron":4,"Cube":6,"Octahedron":8,"Dodecahedron":12,"Icosahedron":20}
ans=0
n=int(input())
for i in range(n):
    ans+=d[input()]
print(ans)
