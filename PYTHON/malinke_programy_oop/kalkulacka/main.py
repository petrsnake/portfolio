from kalkulacka import Kalkulacka

vypocet = Kalkulacka()
vypocet.prvni = float(input('Zadejte prvni cislo: '))
vypocet.druhy = float(input('Zadejte druhe cislo: '))
print('součet je: {0}'.format(vypocet.scitani()))
print('rozdíl je: {0}'.format(vypocet.odcitani()))
print('násobek je: {0}'.format(vypocet.nasobeni()))
print('rozdíl je: {0}'.format(vypocet.deleni()))
