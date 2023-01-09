#délka jména
a = input('Napiš své jméno: ')
if (len(a) > 3 and len(a) < 10):
    print('Tvé jméno je normálně dlouhé...')
elif len(a) <= 3:
    print('Tvé jméno je krátké...')
elif len(a) >= 10:
    print('Tvé jméno je dlouhé...')
else:
    print('Chybné zadání')