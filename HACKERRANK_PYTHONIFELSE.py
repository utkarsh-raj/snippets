# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:30:29 2019

@author: Divyanshi
"""
n=int(input())
c=n%2
if (c!=0):
    print("Weird")
if (c==0):
    if (2<=n<=5):
        print("Not Weird")
    elif (6<=n<=20):
        print("Weird")
    else:
        print("Not Weird")