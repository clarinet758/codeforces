#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

n,k,a,b=[int(i) for i in input().split()]
x=a
y=b
chk=-1
ans=''

while len(ans)<=n:
    if x==y:
        if len(ans) and ans[-1]=='G':
            ans+='BG'*((n+1)//2)
        else:
            ans+='GB'*((n+1)//2)
        break
    elif chk==0 or (chk==-1 and x>y):
        t=min(k,max(1,x-y))
        ans+='G'*t
        x-=t
        chk=1
    elif chk==1 or (chk==-1 and x<y):
        t=min(k,max(1,y-x))
        ans+='B'*t
        y-=t
        chk=0
ans=ans[:n]
print(ans if (ans.count('G')==a and ans.count('B')==b) else 'NO')
