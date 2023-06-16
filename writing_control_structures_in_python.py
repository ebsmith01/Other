# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 16:43:23 2023

@author: EvinSmith
"""


#String parsing 
string = 'X-DSPAM-Confidence: 0.8475'

col_pos = string.find(':')                  
number = string[col_pos+1:]
num = float(number)                  
print(num)

# Control Structures                                   
for i in range(10):
    for j in range(i):
        print ('* ', end="")
    print('')                                                                                                               

for i in range(10,0,-1):
    for j in range(i):  
        print('* ', end="")
    print('')


# Conditional Looping 
numlist=[]

for i in range(51):
    if i % 3 == 0 and i % 5 == 0:
        print("All Criteria Met")
        continue
    elif i % 5 == 0:
        print("Second Critera Met")
        continue
    elif i % 3 == 0:
        print("First Critera Met")
        continue
    print(i)

# Return all numbers in a list that are divisible by 5 and 7
for i in range(1, 2700):
    if (i%7==0) and (i%5==0):
        numlist.append(str(i))
print (','.join(numlist))


# return data types of items in a list 
data = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}]
for item in data:
   print ("Type of ",item, " is ", type(item))


