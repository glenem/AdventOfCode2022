# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:01:51 2022

@author: glenm

Part 1 Goal?

Assumptions: 
    The start of a packet is indicated 
    by a sequence of four characters that 
    are all different
    
    Can only begin after four characters
    
Goal:
    We are looking for the mumber of characters 
    or the length of a string from the start (position 0) 
    to the last character to our unique four character sequence  

Question:
    How many characters need to be processed before the first start-of-packet marker is detected?
    
"""

"""
Part 1 Algorithm (Naive Solution: Character Snake):
    1. Start with the first 4 characters of the string
    2. Detect if any one of the 4 characters are the same
    3. If so stop and return the index of the 4th character
    4. If not increment the position of character 1 through character 4 by 1 move
    5. Repeat 2 until we get the answer through recurssion

"""

with open('Day6.txt', 'r+') as F:
    Ex1D6 = F.readline()

def Day6Tk1Sol(Input):
    # Positional variable
    c1 = 0
    c2 = 1
    c3 = 2
    c4 = 3
    
    t = 0
    
    while t < len(Input)-1:
        # If statement indicating wheter the 4 character sequence contains all unique characters.
        if Input[c1] == Input[c2] or Input[c1] == Input[c3] or Input[c1] == Input[c4] \
        or Input[c2] == Input[c3] or Input[c2] == Input[c4] or Input[c3] == Input[c4]:
            # Index movers
            c1 = c1 + 1
            c2 = c2 + 1
            c3 = c3 + 1
            c4 = c4 + 1
            # time counter
            t = t + 1
            
        else:
            # answer (adds a one to get to the end of the 4th character in the unique string)
           return c4 + 1 
      

'''
Part 2: 
    Asumption:
        Messages are a unique sequence of 14 characters
    Question:
        How many characters need to be processed before 
        the first start-of-message marker is detected?
'''

from collections import Counter

def Day6GenSol(InputData, begin, end):
    
    t = 0
    
    while t < len(InputData):
        string = InputData[begin:end]
        freq = Counter(string)
        
        if len(freq) == len(string):
            return end
        
        else:
            begin = begin + 1 
            end = end + 1
            t = t + 1
'''
# Task 1 solution
print(Day6GenSol(Ex1D6, begin=0, end=3))
# Task 2 solution
print(Day6GenSol(Ex1D6, begin=0, end=14))
'''

c = Counter("abc")
print(c)
print(len(c))
c1 = Counter("aav")
print(c1)
print(len(c1))