# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 17:35:05 2022

Advent of Code Day 1 Challenge.

Goal:
Find the Elf carrying the most Calories. 
How many total Calories is that Elf carrying?    

@author: glenm
"""

# Part 1 Code
def OpenText(Data):
    F = open(Data, 'r+')
    lines = [line for line in F.readlines()]
    F.close()
    
    return lines
    
def Day1_Sol(InputData):
    # A variable to generate the sum of calories per elf
    counter = 0
    # An array to store the sum of calories per elf
    Data = []
    for Calorie in InputData:
        
        if len(Calorie) != 1:
            counter = counter + int(Calorie)
            
            if Calorie == InputData[len(InputData)-1]:
                Data.append(int(Calorie))
            
        elif len(Calorie) == 1:
            Data.append(counter)
            counter = 0       
    
    return Data
'''
print(Day1_Sol(Example1))
'''

Day1 = OpenText('Day1.txt')
Day1_Calories = Day1_Sol(Day1)

# print(max(Day1_Calories))

# Part 2 Code How many calories are the top three Elves carrying
Day1_Calories.sort(reverse=True)

Top3_Calories = 0

for item in list(range(0, 3)):
    Top3_Calories = Top3_Calories + Day1_Calories[item]

# print(Top3_Calories)

# Output Text File

def new_file(file, part1, part2):
    f = open(file, "w")
    
    f.write("Advent of Code 2022 Day 1 Solutions \n")
    
    f.write("Part 1: " + str(max(part1)) + "\n")
    
    f.write("Part 2: " + str(part2) + "\n")
    
    f.close()
    
new_file('Day1_Solutions.txt', Day1_Calories, Top3_Calories)
