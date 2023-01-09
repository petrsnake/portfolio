class Kostka:
    """
    Třída reprezentuje hrací kostku
    """
    def __init__(self, pocet_stran:int=6) -> None:
        self.__pocet_stran = pocet_stran

    def __str__(self) -> str:
        """
        Vrací text reprezentující kostku
        """
        return str('Kostka s {0} stěnami'.format(self.__pocet_stran))

    def vrat_pocet_stran(self):
        """
        Vrátí počet stran kostky
        """
        return self.__pocet_stran

    def hod(self):
        """
        Vykoná hod kostkou od 1 do počtu stran
        """
        import random as _random
        return _random.randint(1, self.__pocet_stran)



