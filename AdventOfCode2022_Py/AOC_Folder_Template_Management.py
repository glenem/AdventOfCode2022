# -*- coding: utf-8 -*-
"""
@author: glenm

Creates folders and files for all of the Advent Of Code Days

"""

import os
import shutil

directory = os.getcwd()

start = 1
end = 25

AOC_Template = directory + "\Advent Of Code Day\AOC_Template.py"
Day_text = directory + "\Advent Of Code Day\Day.txt"
ExDay_text = directory + "\Advent Of Code Day\ExDay.txt"

file_list_from = [AOC_Template, Day_text, ExDay_text]

file_list_to = ["\AOC_Day.py", 
                "\Day.txt",
                "\ExDay.txt"]

for t in range(start, end+1):
    
    newpath = directory + "\Advent Of Code Day " + str(t)

    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    for i in [0, 1, 2]:
        shutil.copyfile(
            file_list_from[i], 
            directory + "\Advent Of Code Day " + str(t) + file_list_to[i]
            )
    
    file_list_to2 = ["\AOC_Day"+str(t)+".py", 
                    "\Day"+str(t)+".txt",
                    "\ExDay"+str(t)+".txt"]
    
    for m in [0, 1, 2]:
        
        os.rename(directory + "\Advent Of Code Day " + str(t) + file_list_to[m],
                  directory + "\Advent Of Code Day " + str(t) + file_list_to2[m])