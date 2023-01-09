def is_win_row(playground:list):
    '''
    Funkce na detekci výhry v řádku
    '''
    win = False
    for i in playground:
        test_str = ''
        for j in i:
            test_str += str(j)

        if ('xxxxx' in test_str):
            print('Výhercem se stává hráč číslo 1!\n')
            win = True
        elif ('ooooo' in test_str):
            print('Výhercem se stává hráč číslo 2!\n')
            win = True

    return win

def is_win_col(playground:list):
    '''
    Funkce na detekci výhry ve sloupci
    '''
    win = False

    for i in range(1,9):
        col_str = ''
        for j in range(1,10):
            col_str += playground[j][i]

        if ('xxxxx' in col_str):
            print('Výhercem se stává hráč číslo 1!\n')
            win = True
        elif ('ooooo' in col_str):
            print('Výhercem se stává hráč číslo 2!\n')
            win = True

    return win