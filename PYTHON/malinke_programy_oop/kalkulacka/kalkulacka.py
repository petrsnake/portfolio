class Kalkulacka():
    """
    Tato třída slouží jako základní kalkulačka
    """
    prvni = ''
    druhy = ''

    def scitani(self):
        """
        vrátí součet
        """
        return self.prvni + self.druhy
    
    def odcitani(self):
        """
        vrátí rozdíl
        """
        return self.prvni - self.druhy

    def nasobeni(self):
        """
        vrátí násobek
        """
        return self.prvni * self.druhy

    def deleni(self):
        """
        vrátí součin
        """
        return self.prvni / self.druhy