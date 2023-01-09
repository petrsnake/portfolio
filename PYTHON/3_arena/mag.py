from bojovnik import Bojovnik
class Mag(Bojovnik):
    """
    Mág je dceřinná třída od Bojovníka.
    Mág manu, která dává větší útok při plném nabytí. Pak se nabíjí každé kolo 10 many.
    """

    def __init__(self, jmeno, zivot, utok, obrana, kostka, mana, magicky_utok):
        super().__init__(jmeno, zivot, utok, obrana, kostka)
        self._mana = mana
        self._max_mana = mana
        self._magicky_utok = magicky_utok

    def utoc(self, souper):
        #mana není plná
        if self._mana < self._max_mana:
            self._mana += 10
            if self._mana > self._max_mana:
                self._mana = self._max_mana
            super().utoc(souper)
        #magický útok
        else:
            uder = self._magicky_utok + self._kostka.hod()
            zprava = f'{self._jmeno} použil magii za {uder} hp.'
            self._nastav_zpravu(zprava)
            self._mana = 0
            souper.bran_se(uder)
        
    def graficka_mana(self):
        #grafický ukazatel many
        return self.graficky_ukazatel(self._mana, self._max_mana)

    def _vypis_bojovnika(self, bojovnik):
        #výpis mága
        print(bojovnik)
        print("Život: {0}".format(bojovnik.graficky_zivot()))
        if isinstance(bojovnik, Mag):
            print("Mana: {0}".format(bojovnik.graficka_mana()))

