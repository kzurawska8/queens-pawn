import random
import os

def generowanie_mapy():
    plansza = []
    plansza.append([" "] + [str(i) for i in range(1, 9)])
    for wiersz in range(1, 9):
        plansza.append([str(wiersz)] + ["." for _ in range(8)])
    return plansza

def ustaw_hetmanow(plansza, k):
    hetmani = []
    for hetman in range(k):
        n = random.randint(1, 8)
        m = random.randint(1, 8)
        while (n, m) in hetmani:
            n = random.randint(1, 8)
            m = random.randint(1, 8)
        hetmani.append((n, m))
        plansza[n][m] = 'H'
    return hetmani

def ustaw_pionka(plansza, hetmani):
    n = random.randint(1, 8)
    m = random.randint(1, 8)
    while (n, m) in hetmani:
        n = random.randint(1, 8)
        m = random.randint(1, 8)
    plansza[n][m] = 'P'
    return (n, m)

def wyswietl_mape(plansza):
    print()
    for wiersz in plansza:
        print("  ".join(wiersz))
    print()

def czy_atakowany(hetman, pionek):
    if hetman[0] == pionek[0] or hetman[1] == pionek[1] or abs(hetman[0] - pionek[0]) == abs(hetman[1] - pionek[1]):
        return True
    return False

def weryfikacja_bicia(hetmani, pionek):
    atakujacy_hetmani = []
    for hetman in hetmani:
        if czy_atakowany(hetman, pionek):
            atakujacy_hetmani.append(hetman)
    return atakujacy_hetmani

def przestaw_pionka(plansza, pionek, hetmani):
    plansza[pionek[0]][pionek[1]] = '.'
    return ustaw_pionka(plansza, hetmani)

def usun_hetmana(plansza, hetmani, pozycja):
    if plansza[pozycja[0]][pozycja[1]] == 'H':
        plansza[pozycja[0]][pozycja[1]] = '.'
        hetmani.remove(pozycja)
    else:
        print(f"\nNie ma hetmana na pozycji {pozycja}")

k = int(input("Podaj liczbę hetmanów (max 5): "))

if k < 0 or k > 5:
    raise ValueError("Only positive integers less than 5 are allowed")

plansza = generowanie_mapy()
hetmani = ustaw_hetmanow(plansza, k)
pionek = ustaw_pionka(plansza, hetmani)
wyswietl_mape(plansza)
atakujacy_hetmani = weryfikacja_bicia(hetmani, pionek)

if atakujacy_hetmani:
    print("Pionek jest zagrożony przez hetmanów na pozycjach:")
    for hetman in atakujacy_hetmani:
        print(hetman)
    print()
else:
    print("Pionek nie jest zagrożony przez żadnego hetmana.\n")

while True:
    try:
        opcja = int(input("1) Wylosowanie nowej pozycji dla pionka z pozostawieniem pierwotnego układu hetmanów;\n2) Usunięcie dowolnego hetmana (wskazanie jego pozycji);\n3) Ponowna weryfikacja bicia po ustaleniu zmian;\n4) Wyjście;\nOpcja: "))
    except ValueError:
        print("\nNie ma takiej opcji. Spróbuj jeszcze raz.\n")
        continue

    if opcja == 1:
        pionek = przestaw_pionka(plansza, pionek, hetmani)
        os.system("cls")
        wyswietl_mape(plansza)
        continue
    elif opcja == 2:
        pozycja = tuple(map(int, input("\nPodaj pozycję hetmana do usunięcia ('x y'): ").split()))
        usun_hetmana(plansza, hetmani, pozycja)
        os.system("cls")
        wyswietl_mape(plansza)
        continue
    elif opcja == 3:
        os.system("cls")
        wyswietl_mape(plansza)
        atakujacy_hetmani = weryfikacja_bicia(hetmani, pionek)
        if atakujacy_hetmani:
            print("Pionek jest zagrożony przez hetmanów na pozycjach:")
            for hetman in atakujacy_hetmani:
                print(hetman)
        else:
            print("Pionek nie jest zagrożony przez żadnego hetmana.\n")
        break
    elif opcja == 4:
        break