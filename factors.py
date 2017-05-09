# -*- coding: utf-8 -*-
"""
Created on Mon May  9 21:00:18 2017

@author: kateryna shlapatska
"""
import math

n=int(input("please, enter a number: "))
i=1
r=[]
#limit our checkings for square root of given number, as there are no factors more then sqrt
while(i<=math.sqrt(n)):
    if (n%i==0):
            r.append(i)
            if (i!=n/i):
                r.append(int(n/i))
    i+=1

#print result
j=0
while(j<len(r)):
    print(r[j])
    j+=1