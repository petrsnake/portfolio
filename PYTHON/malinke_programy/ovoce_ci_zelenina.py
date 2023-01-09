'''''''''
ukol1 = list(range(10,0,-1))
print(ukol1)
for i in ukol1:
    print(i)
'''''''''
ovoce = ['jablko', 'hruška', 'malina', 'třešeň']
zelenina = ['brokolice', 'mrkev', 'květák', 'rajče']
odpoved = 'ano'
i=0
while odpoved == 'ano':
    ask = input('Zadej název libovolného ovoce, nebo zeleniny: ')
    i+=1
    if ask in ovoce:
        print(f'{ask} je ovoce!')
    elif ask in zelenina:
        print(f'{ask} je zelenina!')
    else:
        print('Neznámý objekt, zkuste něco jiného')
        continue
    zpatecka = True
    while zpatecka:
        odpoved = input('Přeješ si zadat další slovo? (ano/ne): ')
        if odpoved =='ano':
            zpatecka = False
        elif odpoved =='ne':
            print(f'zeptal ses na {i} subjektů')
            zpatecka = False
        else:
            print('odpovídej pouze (ano/ne)')
            zpatecka = True
        

