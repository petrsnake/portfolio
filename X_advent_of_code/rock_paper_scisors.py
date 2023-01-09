"""
oponent:
A = rock, B = paper, C = scissors
you:
X = rock = 1, Y = paper = 2, Z = scissors = 3
X = lose, Y = draw, Z = win
lost = 0, draw = 3, win = 6
"""

from strategy_guide import strategy as guide
    symbol_score = {'X' : int(1),'Y' : int(2), 'Z' : int(3)}

def score_counter(guide:str):
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

    #counting of score by rules        
    score = 0
    cykl = int(0)

    #points for your symbol
    for pair in fin_list_guide:
        print(f'prubeh cyklem č. {cykl} s párem {pair}')
        your_move = pair[1]
        score += symbol_score[your_move]
        print(f'skore za symbol {symbol_score[your_move]}')

        #points for win, or match
        if pair == 'AX' or pair == 'BY' or pair == 'CZ':
            score += 3
            print('+3 za remízu')
        elif pair == 'CX' or pair == 'AY' or pair == 'BZ':
            score += 6
            print('+6 za výhru')

        print(f'{score}\n')
        cykl +=1
    return score
            
print(score_counter(guide))