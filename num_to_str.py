# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 18:16:10 2018
convert number to string format 99,99,999
@author: ch@tur
"""

num=int(input("Enter any positive number: "))

n=num
w=""
k=0
while(n>0):
    r=str(n%10)
    n=int(n/10)
    if(len(w)-k==3):
        k=len(w)
        w=w+","+r
    else:
        w=w+""+r

w=w[::-1]
print("Result: "+w)