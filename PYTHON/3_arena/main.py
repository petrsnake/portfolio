from kostka import Kostka
from bojovnik import Bojovnik
from arena import Arena
from mag import Mag

# vytvoření kostky, zápasníků do arény a arény
kostka = Kostka(10)
balrog = Bojovnik("Balrog", 200, 20, 10, kostka)
gandalf = Mag("Gandalf", 80, 18, 15, kostka, 30, 45)
arena = Arena(balrog, gandalf, kostka)

# zápas
arena.zapas()
input()
