
#test palindromu
slovo = input('napiš slovo: ')
opak = slovo[::-1]
puldelka = len(slovo)//2
if slovo[0:puldelka] == opak[0:puldelka]:
    print(f'slovo {slovo} je palindrom')
else:
    print(f'slovo {slovo} není palindrom')

