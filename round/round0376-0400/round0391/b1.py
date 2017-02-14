#!/usr/bin/env pypy3
# -*- coding: UTF-8 -*-

def prime_t(t):
    i=2
    while i**2<=t:
        if t%i==0:
            return 0
        i+=1
    return 1

def prime_list(tt):
    p_list=[]
    for i in range(2,tt+1):
        if prime_t(i):
            p_list.append(i)
    return p_list

#317まで、317*317=100489、、までの素数を用意
chk=prime_list(318)
#317までの素数を個別にと、+1で確保したものは適当に使う
ans=[0]*(len(chk)+1)
ans[-1]=1
n=int(input())
#1はいらないので捨てる
l=[int(i) for i in input().split() if i!='1']

d={}
#同じ数がそれぞれ何個あるかを連想配列にいれる
#ans[-1]には最大の個数を入れておく、現時点では解の有力候補
for i in l:
    if i in d:
        d[i]+=1
        ans[-1]=max(ans[-1],d[i])
    else:
        d[i]=1

#重複してるものの個数を数え終わったのでsetで重複排除する
l=list(set(l))
l.sort()

#それぞれの数を317までの素数で割り切れなくなるまで割る
#317より大きな素数は新たな連想配列に入れて個数を数える
#317より大きい素数の個数とans[-1]を比較して大きければ更新する
over={}
for i in l:
    tmp=i
    for j,k in enumerate(chk):
        if i%k==0:
            ans[j]+=d[tmp]
            while i%k==0:
                i//=k
        if i<k:
            break
    if i>317:
        if i in over:
            over[i]+=d[tmp]
            ans[-1]=max(ans[-1],over[i])
        else:
            over[i]=d[tmp]
#ansのなかで最大のものが解になる
print(max(ans))
