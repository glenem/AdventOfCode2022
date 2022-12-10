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
    
    list_of_lists = []
    
    # Converts each string to a list of charcters and puts them in one list
    # Hence we have a list which contains lists of strings
    for string in lines2:
        list_of_lists.append(list(string))
    
    integer_lists_of_lists = []
    # Converts the strings to ints so because their numerical value is important
    for lists in list_of_lists:
        integer_lists_of_lists.append(list(map(int, lists)))
        
    return integer_lists_of_lists
'''
Part 1
'''
Example1 = OpenText("ExDay8.txt")
def Task1_Ver1 (A):
    
    v1 = 2*(len(A)-1) + 2*(len(A[0])-1)
    
    Dict1 = {}
    
    # Check Top 
    for i in range(1, len(A)-1):
        for j in range(1, len(A[0])-1):
            Top = []
            for k in range (i-1, -1, -1):
                Top.append(A[k][j])
                
            if A[i][j] > max(Top):
                    Dict1[str(i)+","+str(j)] = A[i][j]
            else:
                pass
            
    # Check Bottom 
    for i in range(1, len(A)-1):
        for j in range(1, len(A[0])-1):
            Bottom = []
            for k in range (i+1, len(A)):
                Bottom.append(A[k][j])
                
            if A[i][j] > max(Bottom):
                    Dict1[str(i)+","+str(j)] = A[i][j]
            else:
                pass
    
    # Check Bottom 
    for i in range(1, len(A)-1):
        for j in range(1, len(A[0])-1):
            Left = []
            for k in range (j-1, -1, -1):
                Left.append(A[i][k])
                
            if A[i][j] > max(Left):
                Dict1[str(i)+","+str(j)] = A[i][j]
            else:
                pass
    
    # Check Bottom 
    for i in range(1, len(A)-1):
        for j in range(1, len(A[0])-1):
            Right = []
            for k in range (j+1, len(A[i])):
                Right.append(A[i][k])
                
            if A[i][j] > max(Right):
                Dict1[str(i)+","+str(j)] = A[i][j]
            else:
                pass
    return len(Dict1) + v1
    #return v1+v2

#print(Task1_Ver1(Example1))
print(Task1_Ver1(OpenText("Day8.txt")))


'''
Part 2
'''