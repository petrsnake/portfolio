class Bezec():
    """
    Třída reprezentuje běžce, který může spát, běhat a hlídá se mu únavu
    """
    def __init__(self, jmeno:str) -> None:
        self.__jmeno = jmeno
        self.__unava = 0
    
    def beh(self, kilometry:int):
        self.__unava += kilometry
        if self.__unava > 20:
            self.__unava -= kilometry
            print('Jsem příliš unavený')

    def spanek(self, hodiny:int):
        self.__unava -= hodiny * 10
        if self.__unava < 0:
            self.__unava = 0



    def __str__(self) -> str:
        return str('{0} {1}'.format(self.__jmeno, self.__unava))

karel = Bezec('Karel Kakol')
karel.beh(10)
karel.beh(10)
karel.beh(10)
print(karel)
karel.spanek(2)
print(karel)
karel.beh(20)
print(karel)