# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:41:42 2022

@author: glenm
"""

"""
Day 2 Part 1
What would your total score be if everything goes exactly according to your strategy guide?

Game Logic

The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)

"""

# Part 1 Solution

def OpenText(Data):
    F = open(Data, 'r+')
    lines = [line for line in F.readlines()]
    F.close()
    
    return lines

Day2 = OpenText("Day2.txt")

Opp = []
You = []

for Day in Day2:
    Day.split(" ")
    Opp.append(Day[0])
    You.append(Day[2])
    
    

game_dic_opp = {'A':'Rock', 'B':'Paper', 'C':'Scissors'}
game_dic_you = {'X':'Rock', 'Y':'Paper', 'Z':'Scissors'}

Opp_Game = [game_dic_opp.get(n, n) for n in Opp]

You_Game = [game_dic_you.get(n, n) for n in You]

def GamePlay(Opp, You):
    
    score = []

    draw = 3
    win = 6

    rock = 1
    paper = 2
    scissors = 3
    
    for game in range(0,len(Opp)):
        
        if Opp[game] == "Rock":
            if You[game] == "Rock":
                score.append(rock + draw)
            elif You[game] == "Scissors":
                score.append(scissors)
            else: 
                score.append(win + paper)
        
        elif Opp[game] == "Paper":    
            if You[game] == "Rock":
                score.append(rock)
            elif You[game] == "Paper":
                score.append(paper + draw)
            else:
                score.append(win + scissors)
        
        elif Opp[game] == "Scissors":    
            if You[game] == "Scissors":
                score.append(scissors + draw)
            elif You[game] == "Paper":
                score.append(paper)
            else:
                score.append(win + rock)

    return sum(score)

print(GamePlay(Opp=Opp_Game, You=You_Game))


'''
The Elf finishes helping with the tent and sneaks back over to you. 
"Anyway, the second column says how the round needs to end: 
X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. 
Good luck!"
'''

game_dic_you2 = {'X':'Lose', 'Y':'Draw', 'Z':'Win'}

You_Game2 = [game_dic_you2.get(n, n) for n in You]

def GamePlay2(Opp, You):
    
    score = []

    draw = 3
    win = 6

    rock = 1
    paper = 2
    scissors = 3
    
    for game in range(0,len(Opp)):
        
        if Opp[game] == "Rock":
            if You[game] == "Draw":
                score.append(rock + draw)
            elif You[game] == "Lose":
                score.append(scissors)
            else:
                score.append(win + paper)
        
        elif Opp[game] == "Paper":    
            if You[game] == "Lose":
                score.append(rock)
            elif You[game] == "Draw":
                score.append(paper + draw)
            else:
                score.append(win + scissors)
                
        elif Opp[game] == "Scissors":    
            if You[game] == "Draw":
                score.append(scissors + draw)
            elif You[game] == "Lose":
                score.append(paper)
            else:
                score.append(win + rock)

    return sum(score)

print(GamePlay2(Opp_Game, You_Game2))