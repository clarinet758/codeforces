#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import itertools
n=raw_input()
x=len(n)
sokushi=list(n)
if sokushi.count('4')==sokushi.count('7') and len(sokushi)==(sokushi.count('4')+sokushi.count('7')):
    print n
elif (x%2!=0) or (int(n)>int('7'*(x/2)+'4'*(x/2))):
    print '4'*(x/2+1)+'7'*(x/2+1)
elif int(n)<int('4'*(x/2)+'7'*(x/2)):
    print ('4'*(x/2)+'7'*(x/2))
else:
    jk=['4' for _ in range(x/2)]
    for i in range(x/2):
        jk.append('7')
    kari=[]
    for j in itertools.permutations(jk):
        kari.append(''.join(list(j)))
    kari=set(kari)
    kari=list(kari)
    kari.sort()
    for k in range(len(kari)):
        if int(n)<int(kari[k]):
            print kari[k]
            exit()

