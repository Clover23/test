# -*- coding: utf-8 -*-
"""
Created on Mon May  9 21:30:09 2017

@author: kateryna shlapatska
"""

#function to find longest sequence of 1s in string
def longest(s):
    l=len(s)   
    i=0
    j=i+1    
    r=0
    temp=0
  
    while (i<l):
        if (s[i]=="1"):
            r+=1
            if (j==l):
                break
            if (s[j]=="0"):
                if r>temp:
                    temp=r
                    r=0
                else:
                    r=0
        i+=1
        j+=1
    return max(r, temp)

#create string from content of INPUT file
s1=open("INPUT.txt", "r").read()
#define the length of longest sequence        
p=longest(s1)
#write result in OUTPUT file
file=open("OUTPUT.txt", "w")
file.write(str(p))
file.close() 
   