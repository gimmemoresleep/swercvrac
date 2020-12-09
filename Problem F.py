#!/usr/bin/env python
# coding: utf-8

# In[3]:


#GHARBI MOHAMED  
#Sofian Zerzour
#Johan Laforge

W = 0
N= 0
print("enter the width of the hole cake")
while W < 1 or W > 5000000 :
    W = int(input())   
print("enter the number of the shatered pieces")
while N < 1 or N>10000 :
    N = int(input())
import numpy as np
a=np.zeros((N,2))
print("enter the width and length of each sub piece")
m = 0
l=0
for i in range(N) : 
    while m < 1 or m > 10000 and l < 1 or l > 10000 :
        m = int(input())
        l = int(input())
    a[i,0]=m
    a[i,1]=l
    m = 0
    l=0
length = 0
for i in range(N) : 
    length = length + a[i,0]*a[i,1]
length = length / W
print("the length of the cake is : ",length)