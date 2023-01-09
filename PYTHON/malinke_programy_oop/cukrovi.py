#Využití Factory pro tvorbu cukroví
class Cukrovi():
    
    def __init__(self, barva, tvar, vaha) -> None:
        self.barva = barva
        self.tvar = tvar
        self.vaha = vaha

    def __str__(self):
        return f'Cukrový barvy {self.barva}, tvaru {self.tvar} a váhy {self.vaha}g'

class TovarnaNaCukrovi():

    @staticmethod
    def rohlicky():
        print(Cukrovi('žlutá', 'měsíček', 20))

    @staticmethod
    def linecke():
        print(Cukrovi('zlatá', 'kolečko', 40))

    @staticmethod
    def kokosky():
        print(Cukrovi('bílá', 'hrudky', 15))



