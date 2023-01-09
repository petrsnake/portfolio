class Arena:

    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        self.__bojovnik_1 = bojovnik_1
        self.__bojovnik_2 = bojovnik_2
        self.__kostka = kostka

    def __vykresli(self):
        self.__vycisti_obrazovku()
        print("-------------- Aréna -------------- \n")
        print("Bojovníci: \n")
        self.__bojovnik_1._vypis_bojovnika(self.__bojovnik_1)
        self.__bojovnik_2._vypis_bojovnika(self.__bojovnik_2)
        """
        self._vypis_bojovnika(self.__bojovnik_1)
        self._vypis_bojovnika(self.__bojovnik_2)
        """
        print("")


    def __vycisti_obrazovku(self):
        """
        Vymaže obrazovku konzole.
        """
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call(["clear"])

    def __vypis_zpravu(self, zprava):
        """
        Vypíše zprávu se zpožděním.
        """
        import time as _time
        print(zprava)
        _time.sleep(0.5)

    def zapas(self):
        """
        Simuluje zápas bojovníků.
        """
        import random as _random
        print("Vítejte v aréně!")
        print("Dnes se utkají {0} s {1}!".format(self.__bojovnik_1,
                                                 self.__bojovnik_2))
        print("Zápas může začít...", end=" ")
        input()
        # prohození bojovníků
        if _random.randint(0, 1):
            (self.__bojovnik_1, self.__bojovnik_2) = (self.__bojovnik_2,
             self.__bojovnik_1)
        # cyklus s bojem
        while (self.__bojovnik_1.nazivu and self.__bojovnik_2.nazivu):
            self.__bojovnik_1.utoc(self.__bojovnik_2)
            self.__vykresli()
            self.__vypis_zpravu(self.__bojovnik_1.vrat_posledni_zpravu())
            self.__vypis_zpravu(self.__bojovnik_2.vrat_posledni_zpravu())
            if self.__bojovnik_2.nazivu:
                self.__bojovnik_2.utoc(self.__bojovnik_1)
                self.__vykresli()
                self.__vypis_zpravu(self.__bojovnik_2.vrat_posledni_zpravu())
                self.__vypis_zpravu(self.__bojovnik_1.vrat_posledni_zpravu())
            print("")