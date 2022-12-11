# -*- coding: utf-8 -*-
"""
Advent of Code Day

@author: glenm
"""

"""
Common functions used in all of my AOC code thus far
"""

import re

def OpenText(Data):
    with open(Data, 'r+') as F:
        lines = [line for line in F.readlines()]
    
    lines2 = []
    
    # Removes new lines "\n" they are a pain
    for line in lines:
        lines2.append(line.strip())
    
    Input = []
    for i in range(0, len(lines2)-1):
        x = re.split(" ", lines2[i])
        if x[0] == "addx":
            x[1] = int(x[1])
        else:
            pass
        Input.append(x) 
        
    return Input
def new_file(file, day, part1, part2, year=2022):
    with open(file, "w") as f:
    
        f.write("Advent of Code "+str(year)+" Day "+str(day)+" Solutions \n")
    
        f.write("Part 1: " + str(part1) + "\n")
    
        f.write("Part 2: " + str(part2) + "\n")

Example1 = OpenText("ExDay10.txt")
Day10 = OpenText("Day10.txt")

'''
Part 1
Find the signal strength during 
the 20th, 60th, 100th, 140th, 180th, and 220th cycles. 
What is the sum of these six signal strengths?
'''
class CPU:
    def __init__(self):
        
        '''
        The register, X, for the CPU. 
        Value starts at 1
        '''
        self.X = 1
        self.cycle_X = [self.X]
        '''
        To count the number of cycles 
        during a programs execution
        '''
        self.cycle_counter = 0
        
        ''' 
        To store the cycle number with the value of X
        Only used for the 20th, 60th, 100th, 
        140th, 180th, and 220th cycles)
        '''
        self.cycles = []
    
    def check_cycle(self):
        if self.cycle_counter in range(20, 221, 40):
           self.cycles.append((self.cycle_counter, self.X))
        
    def execute_code(self, code):
        for line in code:
            
            if line[0] == "noop":
                '''
                noop takes 1 cycle to complete
                '''
                self.cycle_counter+=1
                #print(self.cycle_counter)
                self.cycle_X.append(self.X)
                self.check_cycle()
            elif line[0] == "addx":
                ''' 
                addx V takes 2 cycles to complete 
                '''
                c = 0
                while c < 2: 
                    self.cycle_counter+=1
                    self.check_cycle()
                    c+=1
            
                self.X+= line[1]
                self.cycle_X.append(self.X)
                #print(self.cycle_counter)
                #print(self.X)
                
            else:
                pass
            
        
    def signal_strength(self):
        SigStr = 0 
        
        for cycle in self.cycles:
            SigStr+=cycle[0]*cycle[1]
            
        print("Signal strength is: "+str(SigStr))
        return SigStr

# Initalize instance
CathodeRayTube = CPU()
# Run the code
CathodeRayTube.execute_code(Day10)
# Find the signal strength
CathodeRayTube.signal_strength()
'''
Part 2
'''