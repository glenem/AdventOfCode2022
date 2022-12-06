# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 00:08:19 2022

@author: glenm

Advent of Code Day 3 Solution

Problem:
The elf who loaded the rucksacks made a mistake by not placing 
all of the necessary componennts in each compartment of the bag.

The compartments are found by taking the length of each element in the array and spliting it in half

Our goal is to find the letter that each compartment has in common.

Afterwards we can assign a numerical priority to them and find to sum of the priorities of those item types

Algorithm:    

 1. Divide the current input array into two arrays for compartment 1 and compartment 2
 2. Convert the characters to their numerical equivalent from a dictionary
 3. Sort each array
 4. Use binary search to find which character/priority each array has in common
 5. Add the pirority number to a scoring array

"""
import string

def OpenText(Data):
    F = open(Data, 'r+')
    lines = [line for line in F.readlines()]
    F.close()
    
    return lines

# Example file for validation
#Day3 = OpenText("ExDay3.txt")

# Puzzle input file
Day3 = OpenText("Day3.txt")


def binary_search(arr_search, item):
    low = 0
    high = len(arr_search)-1
    
    while low <= high:
        mid = (low + high)
        guess = arr_search[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid +1
    return None

    

def Day3_Task1(data):
    # Scoring file
    score = []

    guide = []

    for char in string.ascii_lowercase:
        guide.append(char)
        
    for char in string.ascii_uppercase:
        guide.append(char)

    scoring_guide = dict(zip(guide, list(range(1, 53))))

    for compar in data:
        n = len(compar)
        
        if n%2 == 0:
            compar1 = compar[0:n//2]
            compar2 = compar[n//2:]
            
        else:
            compar1 = compar[0:(n//2+1)]
            compar2 = compar[(n//2):]
            
        # Decouples a string into an array for each characters
        list1 = []
        for element in range(0, len(compar1)-1):
            list1.append(compar1[element])
        
        list2 = []
        for element in range(0, len(compar2)-1):
            list2.append(compar2[element])
        
            
        # Changes letters for numbers
        list1_num = [scoring_guide.get(n, n) for n in list1]
        list2_num = [scoring_guide.get(n, n) for n in list2]
        
        list1_num.sort()
        
        list2_num.sort()
        
        for i in list1_num:
    
            x = binary_search(list2_num, i)
    
            if x != None:
                helper = x
                break
            else:
                continue
            
        score.append(list2_num[helper])
        
    return sum(score)

print(Day3_Task1(Day3))

# Task 2

def Day3_Task2(Data):
    # Scoring file
    score = []
    
    guide = []
        
    for char in string.ascii_lowercase:
           guide.append(char)
            
    for char in string.ascii_uppercase:
           guide.append(char)
    
    Scoring_guide = dict(zip(guide, list(range(1, 53))))
        
    begin = 0
    end = 2
        
    while end <= len(Day3):
        
        Set1 = set(Data[begin]) 
        Set2 = set(Data[end-1]) 
        Set3 = set(Data[end])    
        
        Set1.discard("\n")
        Set2.discard("\n")
        Set3.discard("\n")
        
        begin = begin + 3    
        end = end + 3
    
        # Finding the common element in all three sets
        common = Set1 & Set2 & Set3
        
        common_list = list(common)
        
        score.append(common_list[0])  
            
    score_num = [Scoring_guide.get(n, n) for n in score]
        
    return sum(score_num)

print(Day3_Task2(Day3))