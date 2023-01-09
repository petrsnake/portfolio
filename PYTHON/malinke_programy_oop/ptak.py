#hladový pták se promění v naštvaného ptáka.
#může být krmen
class Ptak():
    def __init__(self) -> None:
        self.hlad = 0
        self.vaha = 50

    def snez(self, hmotnost_jidla):
        self.hlad -= hmotnost_jidla
        self.vaha += hmotnost_jidla

    def __str__(self):
        return f'Jsem pták s váhou {self.vaha} a hladem {self.hlad}.'

class AngryPtak(Ptak):
    def __init__(self) -> None:
        super().__init__()
        self.vztek = 0

    def provokuj(self, provokace):
        if self.hlad > 0:
            self.vztek += provokace
        else:
            self.vztek += provokace * 2
    
    def __str__(self):
        return f'Jsem angry-pták s váhou {self.vaha} a hladem {self.hlad}, míra mého vzteku je {self.vztek}'
    

ptak = Ptak()
print(ptak)
angryptak = AngryPtak()
print(angryptak)
angryptak.snez(80)
angryptak.provokuj(80)
print(angryptak)
