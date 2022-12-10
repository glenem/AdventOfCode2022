# -*- coding: utf-8 -*-
"""
Advent of Code Day

@author: glenm
"""

"""
Common functions used in all of my AOC code thus far
"""
import re
import matplotlib.pyplot as plt

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
    
    
    Input = []
    for i in range(0, len(lines2)):
        x = re.split(" ", lines2[i])
        x[1] = int(x[1])
        Input.append(x)   
    return Input
'''
Part 1
How many positions does the tail of the rope visit at least once?
'''

Example = OpenText("ExDay9.txt")
Day9 = OpenText("Day9.txt")

class Knots:
   
    # There will be two players one H and the other T
    def __init__(self, player):
        self.player = player
        self.CoordLog = []
        # Starting point for both players
        self.add_coord(0, 0)
        self.Movements = {"R": (1,0), "L":(-1,0), 
                 "U":(0,1), "D":(0,-1)}
    
    def see_coords(self):
        print(self.CoordLog)
    
    def length(self):
        return len(self.CoordLog)
        
    def add_coord(self, x, y):
        self.CoordLog.append((x, y))
    
    def move(self, direction, instruct):
        counter = 0
        while counter < instruct[1]:
            previous_position = self.CoordLog[len(self.CoordLog)-1]
            x = previous_position[0]
            y = previous_position[1]
            self.add_coord(x+self.Movements[direction][0], y+self.Movements[direction][1])
            counter+=1
            
    def head(self, instructions):
        for instruct in instructions:
            if instruct[0] =="U":
                self.move("U", instruct=instruct)
            elif instruct[0] =="D":
                self.move("D", instruct=instruct)
            elif instruct[0] =="L":
                self.move("L", instruct=instruct)
            elif instruct[0] =="R":
                self.move("R", instruct=instruct)
    
    def tail(self, other_coords):
        '''
        --- Rules for tail movement ---
        Tail must always be touching the head:
            Adjacent, Diagonaly adjacent and overlaping count
            
            If the head is two steps directly up, down. left or right from the tail
            then the tail must move one step in that direction
            
            If the head and tail aren't touching and are nto in the same row or column
            then the tail always moves one step diagonally to keep up
        '''
        deltalog = []
        index_of_other_steps = len(other_coords)
        for i in range(1, index_of_other_steps):
            x_h = other_coords[i][0]
            y_h = other_coords[i][1]
            pre_x_h = other_coords[i-1][0]
            pre_y_h = other_coords[i-1][1]
            
            previous_position = self.CoordLog[len(self.CoordLog)-1]
            x_t = previous_position[0]
            y_t = previous_position[1]
            
            delta_x = x_h - x_t
            delta_y = y_h - y_t
            
            deltalog.append((delta_x, delta_y))
            
            # Up
            if delta_x == 0 and delta_y == 2:
                self.add_coord(x_t, y_t+1)
            # Down
            elif delta_x == 0 and delta_y == -2:
                self.add_coord(x_t, y_t-1)
            # Right
            elif delta_x == 2 and delta_y == 0:
                self.add_coord(x_t+1, y_t)
            # Reft
            elif delta_x == -2 and delta_y == 0:
                self.add_coord(x_t-1, y_t)
            
            
            # Decides whether the head, 
            # and tail are touching
            elif delta_x == 0 and delta_y == 0 \
                or delta_x ==1 and delta_y == 0 \
                or delta_x ==1 and delta_y ==1\
                or delta_x==0 and delta_y == 1\
                or delta_x ==-1 and delta_y == 0 \
                or delta_x ==-1 and delta_y ==-1\
                or delta_x==0 and delta_y == -1\
                or delta_x ==-1 and delta_y ==1\
                or delta_x ==1 and delta_y ==-1:
                self.add_coord(x_t, y_t)
            # Decides if the head is diagonal to the tail
            elif delta_x == 1 and delta_y == 2 \
                or delta_x == 1 and delta_y == -2 \
                or delta_x == -2 and delta_y == 1 \
                or delta_x == -2 and delta_y == -1\
                or delta_x == 2 and delta_y == -1\
                or delta_x == 2 and delta_y == 1\
                or delta_x == -1 and delta_y == 2 \
                or delta_x == -1 and delta_y == -2:
                self.add_coord(pre_x_h, pre_y_h)
               
    def unqiue_coords(self):
        unique_coords = set(self.CoordLog)
        return unique_coords
'''
H = Knots(player = "Head")

T = Knots(player = "Tail")

# H.head(Example)
#H.head(Day9)
#T.tail(H.CoordLog)

print("Head")
H.see_coords()
print(H.length())
print("Tail")
T.see_coords()
print(T.length())
print("Places Tail visted")
print(T.unqiue_coords())
print(len(T.unqiue_coords()))
'''

'''
Part 2
How many positions does the tail of the rope visit at least once?
'''
# Intitalizes all Knots
H = Knots("Head")
K1 = Knots("Knot1")
K2 = Knots("Knot2")
K3 = Knots("Knot3")
K4 = Knots("Knot4")
K5 = Knots("Knot5")
K6 = Knots("Knot6")
K7 = Knots("Knot7")
K8 = Knots("Knot8")
K9 = Knots("Knot9/Tail")

Example2 = OpenText("Ex2Day9.txt")

H.head(Example2)
K1.tail(H.CoordLog)
K2.tail(K1.CoordLog)
K3.tail(K2.CoordLog)
K4.tail(K3.CoordLog)
K5.tail(K4.CoordLog)
K6.tail(K5.CoordLog)
K7.tail(K6.CoordLog)
K8.tail(K7.CoordLog)
K9.tail(K8.CoordLog)
print(K9.CoordLog)
#print(len(K9.unqiue_coords()))