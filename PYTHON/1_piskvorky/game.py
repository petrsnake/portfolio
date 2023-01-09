from playground import new_area, write_area, vstup
from is_win import is_win_col, is_win_row

def game_move(playground, sign):
    '''
    Funkce mění vzhled pole dle zadaných hodnot hráčem
    '''
    vstup_zadat = True

    while vstup_zadat:
        x,y = vstup()
        try:
            if playground[y][x] == 'x' or playground[y][x] == 'o':
                print('\nToto pole je už obsazené... Vyberte si prosím jiné pole!')
            else:
                playground[y][x] = sign
                vstup_zadat = False
        except IndexError:
            print('\nZadávejte prosím pouze existující pole!')

    write_area(playground)
    win = is_win_row(playground)

    if not win:
        win = is_win_col(playground)

    return win

def game():
    '''
    Funkce vlastní hry. Funkce obsahuje celou hru
    '''
    win = False

    print('\nToto jsou piškvorky! Přeju hodně zábavy!')
    playground = new_area()
    write_area(playground)    

    while not win:
        #tah prvního hráče
        print('Na řadě je hráč číslo 1')
        sign = 'x'
        win = game_move(playground, sign)

        #tah druhého hráče
        if not win:
            print('Na řadě je hráč číslo 2')
            sign = 'o'
            win = game_move(playground, sign)    

    repeat = True
    while repeat:
        question_newgame = input('Přejete si začít novou hru? (ano/ne): ')
        if question_newgame.lower() == "ano":
            game()
        elif question_newgame.lower() == "ne":
            print('\nDoufám že jste si hru užili. Nashledanou.')
            repeat = False
        else:
            print('\nProsím odpovídejte pouze (ano/ne)')

game()
