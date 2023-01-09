#Kořeny kvadratické funkce
print('Program na výpočet kvadratické rovnice')
print('Tvar rovnice: ax^2+bx+c=0')
a = int(input('zadej koueficient a: '))
b = int(input('zadej koueficient b: '))
c = int(input('zadej koueficient c: '))
D = b ** 2 - 4 * a * c
x1 = (-1 * b + D)/ 2*a
x2 = (-1 * b - D)/ 2*a
print(f'kořeny kvadratické funkce jsou {x1} a {x2}')