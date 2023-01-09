#vstupni hodnoty
slovo = input('zadej slovo: ')
heslo = input('zadej heslo: ')
sifra = []

#cisla z hesla
for i in heslo:
    sifra.append(ord(i)-96)

count = 0
result = []
for i in slovo:

    new_code = (ord(i) + sifra[count])

    while new_code > 122:
        new_code -= 26

    new_sign = (chr(new_code))
    result.append(new_sign)
    count+=1

    if count > len(sifra)-1:
        count -= len(sifra)
    else: continue

print(result)


