"""
oponent:

A = rock, B = paper, C = scissors

you:

rock = 1, paper = 2, scissors = 3
X = lose = 0, Y = draw = 3, Z = win = 6
"""

from strategy_guide import strategy as guide

win_points = {'A':2, 'B':3, 'C':1}
lose_points = {'A':3, 'B':1, 'C':2}
draw_points = {'A':1, 'B':2, 'C':3}

def true_score_counter(guide:str):
    #extracting usable list of pairs from elf guide data
    guide = guide.replace(" ", "")
    guide = guide.replace("\n", "")
    guide = list(guide)
    fin_list_guide = []
    for i in guide:
        if i in ['A','B','C']:
            pair = ''
            pair += i
        elif i in ['X', 'Y', 'Z']:
            pair += i
            fin_list_guide.append(pair)

    #counting endgame score
    score = 0
    for pair in fin_list_guide:
        if pair[1] == 'Z':
            score += 6
        elif pair[1] == 'Y':
            score += 3

    
    #counting simbol score
    for pair in fin_list_guide:
        if pair[1] == 'X':
            score += lose_points[pair[0]]
        elif pair[1] == 'Y':
            score += draw_points[pair[0]]
        else:
            score += win_points[pair[0]]
    
    return score

print(true_score_counter(guide))
      