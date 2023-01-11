import random
import sys

koloda = {
    "T♠": 11,
    "T♥": 11,
    "T♦": 11,
    "T♣": 11,

    "K♠": 4,
    "K♥": 4,
    "K♦": 4,
    "K♣": 4,

    "D♠": 3,
    "D♥": 3,
    "D♦": 3,
    "D♣": 3,

    "V♠": 2,
    "V♥": 2,
    "V♦": 2,
    "V♣": 2,

    "10♠": 10,
    "10♥": 10,
    "10♦": 10,
    "10♣": 10,

    "9♠": 9,
    "9♥": 9,
    "9♦": 9,
    "9♣": 9,

    "8♠": 8,
    "8♥": 8,
    "8♦": 8,
    "8♣": 8,

    "7♠": 7,
    "7♥": 7,
    "7♦": 7,
    "7♣": 7,

    "6♠": 6,
    "6♥": 6,
    "6♦": 6,
    "6♣": 6
}

rukaComputera = []
rukaIgroka = []
ochkiComputera = 0
ochkiIgroka = 0


def logika(ochki: int, plaer: str, ochki2:int = -1, comp:str = ""):
    if ochki > 21:
        print(plaer + " проиграл(больше 21)")
        sys.exit()
    elif ochki == 21:
        print(plaer + " победил(21 очко)")
        sys.exit()
    if ochki2 != -1:
        if ochki > ochki2:
            print(plaer+" выиграл( "+str(ochki)+" )")
        elif ochki <ochki2:
            print(comp + " выиграл( " + str(ochki2) + " )")
        else:
            print("ничья")
        sys.exit()



def giveCard(koloda: dict, ruka: list, ochki: int):
    a, b = random.choice(list(koloda.items()))
    ruka.append(a)
    ochki += b
    koloda.pop(a)
    # print(ruka, ochki)
    return ochki
    # взять рандомную карту из словаря, положить ее в руку и удалить из словаря


def showHands(rukaC, ochkiC, rukaI, ochkiI):
    print(f"""----------рука компьютера----------
{rukaC}   {ochkiC}
----------рука игрока----------
{rukaI}   {ochkiI}
_______________________________
""")


def pokazKolod(koloda: dict):
    print(koloda)


ochkiComputera = giveCard(koloda, rukaComputera, ochkiComputera)
ochkiIgroka = giveCard(koloda, rukaIgroka, ochkiIgroka)
ochkiIgroka = giveCard(koloda, rukaIgroka, ochkiIgroka)

showHands(rukaComputera, ochkiComputera, rukaIgroka, ochkiIgroka)
logika(ochkiIgroka, "игрок")

while True:
    menu = input("1 добрать,2 стоп")
    if menu == "1":
        ochkiIgroka = giveCard(koloda, rukaIgroka, ochkiIgroka)
        showHands(rukaComputera, ochkiComputera, rukaIgroka, ochkiIgroka)
        logika(ochkiIgroka, " игрок")
    if menu == "2":
        while ochkiComputera < 21 and ochkiComputera < ochkiIgroka:
            ochkiComputera = giveCard(koloda, rukaComputera, ochkiComputera)
        showHands(rukaComputera, ochkiComputera, rukaIgroka, ochkiIgroka)
        logika(ochkiComputera, "компьютер",ochkiIgroka, "игрок")
