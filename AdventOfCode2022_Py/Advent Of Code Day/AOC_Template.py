# -*- coding: utf-8 -*-
"""
Advent of Code Day

@author: glenm
"""

"""
Common functions used in all of my AOC code thus far
"""

def new_file(file, day, part1, part2, year=2022):
    with open(file, "w") as f:
    
        f.write("Advent of Code "+str(year)+" Day "+str(day)+" Solutions \n")
    
        f.write("Part 1: " + str(part1) + "\n")
    
        f.write("Part 2: " + str(part2) + "\n")
        
        
def OpenText(Data):
    with open(Data, 'r+') as F:
        lines = [line for line in F.readlines()]
    
    lines2 = []
    
    # Removes new lines "\n" they are a pain
    for line in lines:
        lines2.append(line.strip())
    
    return lines2


'''
Part 1
'''


'''
Part 2
'''