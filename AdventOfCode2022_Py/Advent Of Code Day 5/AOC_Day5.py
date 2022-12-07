# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:02:04 2022

@author: glenm
"""

from collections import deque # stack datatype
import re # RegEx


stack_list_day5 = [deque("RSLFQ"), deque("NZQGPT"), deque("SMQB"), 
                   deque("TGZJHCBQ"), deque("PHMBNFS"), deque("PCQNSLVG"),
                   deque("WCF"), deque("QHGZWVPM"), deque("GZDLCNR")]

stack_list_Exday5 = [deque("ZN"), deque("MCD"), deque("P")]


def OpenText(Data):
    with open(Data, 'r+') as F:
        lines = [line for line in F.readlines()]
    
    lines2 = []
    
    # Removes new lines "\n" they are a pain
    for line in lines:
        lines2.append(line.strip())
    
    return lines2


ExDay5 = OpenText("ExDay5.txt")
Day5 = OpenText("Day5.txt")

def MoveFromStack(stacks, instructions):
    #print(stacks)
    for instruct in instructions:
        t = 0
        x = re.split("from", re.split('move', instruct)[1])
        y = re.split("to", x[1])
        z = [int(x[0]), int(y[0]), int(y[1])]
        z_re_index = [z[0], z[1]-1, z[2]-1] 
        ts = z_re_index[0]
        
        while t < ts:
            stacks[z_re_index[2]].append(stacks[z_re_index[1]].pop())
            t = t + 1
     #       print(stacks)

    return stacks

def MakeString(data):
    Example = []
    for Ex in data:
        Example.append(Ex.pop())
    letters = Example[0]
    for ex in range(1,len(Example)):
        letters = letters + Example[ex]
    return letters

print("Task 1")
print('Example')
print(MakeString(MoveFromStack(stack_list_Exday5, ExDay5)))
      
print('Day5 Solution')
print(MakeString(MoveFromStack(stack_list_day5, Day5)))
'''
Getting Day 5 task 2 data ready. 
Altered data structure from a list of stacks to a lists of lists
Because lists can pop from any index not just the end
'''
arr_task2_ExDay5 = []
for item in [deque("ZN"), deque("MCD"), deque("P")]:
    arr_task2_ExDay5.append(list(item))
    
arr_task2_Day5 = []
for item in [[deque("RSLFQ"), deque("NZQGPT"), deque("SMQB"), 
                   deque("TGZJHCBQ"), deque("PHMBNFS"), deque("PCQNSLVG"),
                   deque("WCF"), deque("QHGZWVPM"), deque("GZDLCNR")]]:
    arr_task2_Day5.append(list(item))
    
def MoveFromStack_task2(stacks, instructions):
    #print(stacks)
    for instruct in instructions:
        t = 0
        x = re.split("from", re.split('move', instruct)[1])
        y = re.split("to", x[1])
        z = [int(x[0]), int(y[0]), int(y[1])]
        z_re_index = [z[0], z[1]-1, z[2]-1] 
        ts = z_re_index[0]
        
        if ts == 1:
            stacks[z_re_index[2]].append(stacks[z_re_index[1]].pop())
        else:
            while t < ts:
                stacks[z_re_index[2]].append(stacks[z_re_index[1]].pop(len(stacks[z_re_index[1]])-ts))
                t = t + 1
     #       print(stacks)

    return stacks

print(MakeString(MoveFromStack_task2(stack_list_Exday5, ExDay5)))