import tvar

vetve = tvar.Trojuhelnik('zelená', 15, 15, 25)
kmen = tvar.Obdelnik('hnědá', 3, 26)

print(f'Obsah stromu je {vetve.obsah * 4 + kmen.obsah} cm^2')
