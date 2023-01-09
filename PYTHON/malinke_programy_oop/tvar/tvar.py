class Tvar():
    """Předek všech geometrických tvarů. Má barvu"""

    def __init__(self, barva) -> None:
        self.barva = barva
        
class Obdelnik(Tvar):
    """geometrický tvar obdelnik. Má barvu, sirku a vysku"""

    def __init__(self, barva, sirka, vyska) -> None:
        super().__init__(barva)
        self.sirka = sirka
        self.vyska = vyska

    @property
    def obsah(self):
        """vrátí obsah obdelniku"""
        return (self.sirka * self.vyska)

class Trojuhelnik(Tvar):
    """geometrický tvar trojuhelnik. Má barvu, a delky stran a, b, c."""

    def __init__(self, barva, a, b, c) -> None:
        super().__init__(barva)
        self.a = a
        self.b = b
        self.c = c

    @property
    def obsah(self):
        """vrátí obsah trojuhelníku."""
        import math as _math
        s = (self.a + self.b + self.c) / 2
        S = _math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return S