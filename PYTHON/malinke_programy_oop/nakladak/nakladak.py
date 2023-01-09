class Nakladak():
    """
    Třida nakladniho auta má kapacitu 3 tuny a dá se do ni nakladat a vykladat naklad
    """
    kapacita = 3000
    nalozeno = 0

    def nalozit(self, nakladame:float):
        """
        nalozeni nakladu
        """
        if (self.nalozeno + nakladame) < self.kapacita:
            self.nalozeno += nakladame
        else:
            print('tento náklad nemůže být naložen')

    def vylozit(self, vykladame:float):
        """
        vylozeni nakladu
        """
        if (self.nalozeno - vykladame) >= 0:
            self.nalozeno -= vykladame
        else:
            print('tento naklad nemuze byt vylozen')

    def misto(self):
        """
        podá informace o množství naloženého nákladu
        """
        print(f'v nakladaku je naloženo {self.nalozeno}kg nákladu')