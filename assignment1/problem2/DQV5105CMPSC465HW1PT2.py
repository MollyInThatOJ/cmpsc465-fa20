# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 21:14:50 2020

@author: mama
"""

line1 = input()
line2 = [int(i) for i in input().split()]

n1 = line1[0]
n2 = line2[0]
sortedout = [None]*(n1)

i = 0
k = 0

for i in line2:
    if i==min(line2):
        sortedout[k] = min(line2)
        print(line2[min(line2)])
        line2.pop(line2[i])
        k+=1

    
out =str(sortedout[0])
for i in sortedout[1:]:
    out+=' '+str(i)
    
print(out)