class MujList():
#implementace zakladnich matematickych operaci na třídu MujList

    def __init__(self, list:list) -> None:
        self.list = list

    def __add__(self, other):
        sectene_matice = []
        counter = 0
        for i in self.list:
            sectene_matice.append(i + other.list[counter])
            counter += 1 
        return sectene_matice

    def __sub__(self, other):
        odectene_matice = []
        counter = 0
        for i in self.list:
            odectene_matice.append(i + other.list[counter])
            counter += 1
        return odectene_matice

    def __mul__(self, other):
        nasobek_matice = []
        counter = 0
        for i in self.list:
            nasobek_matice.append(i * other.list[counter])
            counter += 1 
        return nasobek_matice

    def __truediv__(self, other):
        deleni_matice = []
        counter = 0
        for i in self.list:
            deleni_matice.append(i / other.list[counter])
            counter += 1 
        return deleni_matice


a = MujList([1, 10, 3, 4])
b = MujList([1, 5, -3, 4])
print(a / b)
            

