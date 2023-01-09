class Dum():
    #Tvorba domu s byty, kde lze bytové jednotky obsazovat, nebo vylidňovat.


    def __init__(self, byty:int) -> None:
        self.byty = byty
        self.dum = {}
        for i in range(byty+1):
            self.dum[i] = None

    def __getitem__(self, index):
        return self.dum[index]

    def __setitem__(self, key, value):
        if (key <= self.byty and key >= 0): 
            self.dum[key] = value
        else: print('V domě není takový byt')

    def __str__(self) -> str:
        odezva = ''
        for i in range(self.byty+1):
            if (self.dum[i] != None):
                odezva += f'V bytě číslo {i} je {self.dum[i]}\n'
            else:
                odezva += f'Byt číslo {i} je na prodej\n'
        return odezva

chaloupka = Dum(3)
chaloupka[2] = 'tonda'
chaloupka[3] = 'jirka'
print(chaloupka)