# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 15:40:38 2020

@author: s
"""


#n=int(input())
#loc=list(map(int,input().split()))
#m=int(input())
#cabin=list(map(int,input().split()))
#min=0

n,m=3,3
loc=[1,8,2]
cabin=[-3,10,6]
less=0
for i in range(n):
    avail=[]
    com=[]
    for j in  range(m):
        avail.append(abs(loc[i]-cabin[j]))
    
    inx = [i for i, x in enumerate(avail) if x == min(avail)]
    print(inx)
    res_list = [cabin[i] for i in inx] 
    print(res_list.index(min(res_list)))