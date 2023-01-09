class Random_veta():
    """
    třída generuje náhodné věty
    """
    def jaky(self):
        """
        vratí přídavné jméno
        """
        self.__jaky = ['Velký', 'Malý', 'Ošklivý', 'Zelený', 'Starý', 'Barevný', 'Milý', 'Zlý']
        import random as _random
        return _random.choice(self.__jaky)

    def podmet(self):
        """
        vrátí podmět věty
        """
        self.__podmety = ['Pepa', 'papoušek', 'táta', 'želvák', 'banán', 'lotr', 'šampón', 'šmoula']
        import random as _random
        return _random.choice(self.__podmety)

    def sloveso(self):
        """
        vrací sloveso věty
        """
        self.__sloveso = ['pil', 'blil', 'snědl', 'koukal', 'foukal','spal', 'vrávoral']
        import random as _random
        return _random.choice(self.__sloveso)

    def __str__(self):
        """
        vrací hotovou větu
        """
        return '{0} {1} {2}.'.format(self.jaky(), self.podmet(), self.sloveso())

veta = Random_veta()
print(veta)
    