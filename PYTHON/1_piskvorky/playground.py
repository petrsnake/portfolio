def new_area():
    '''
    tvorba nového pole
    '''

    #surové pole
    game_area = []
    for i in range(10):
        column = []
        for j in range(10):
            column.append(" ")
        game_area.append(column)

    #číslování hlavičky
    numbers = [0,1,2,3,4,5,6,7,8,9]
    game_area[0] = numbers
    for i in range(10):
        game_area[i][0] = numbers[i]

    return game_area 

def write_area(pole):
    '''
    výpis stavu pole
    '''
    print()
    for i in pole:
        for j in i:
            print(j, end='')
        print(end='\n')
    print()

def vstup():
    '''
    vstup hráče
    '''
    vstup_zadat = True
    while vstup_zadat:
        try:
            pos_x = int(input('Zadej pozici X, kam chceš táhnout: '))
            pos_y = int(input('Zadej pozici Y, kam chceč táhnout: '))
            vstup_zadat = False
        except ValueError:
            print('\nNeplatný vstup, zadávejte pouze celá čísla 1-9!')
    return pos_x, pos_y

