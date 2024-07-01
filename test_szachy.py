import pytest
from szachy import *

def test_generowanie_mapy():
    plansza = generowanie_mapy()
    assert len(plansza) != 0

def test_ustaw_hetmanow():
    plansza = generowanie_mapy()
    hetmani = ustaw_hetmanow(plansza, 5)
    assert len(hetmani) == 5

def test_ustaw_pionka():
    plansza = generowanie_mapy()
    hetmani = ustaw_hetmanow(plansza, 5)
    pionek = ustaw_pionka(plansza, hetmani)
    assert pionek != 0

def test_czy_atakowany():
    assert czy_atakowany((7, 3), (7, 1)) == True
    assert czy_atakowany((7, 6), (7, 1)) == True
    assert czy_atakowany((6, 8), (7, 1)) == False
    assert czy_atakowany((8, 3), (7, 1)) == False
    assert czy_atakowany((8, 5), (7, 1)) == False
    assert czy_atakowany((6, 8), (3, 5)) == True
    assert czy_atakowany((8, 5), (3, 5)) == True
    assert czy_atakowany((7, 3), (3, 5)) == False
    assert czy_atakowany((7, 6), (3, 5)) == False
    assert czy_atakowany((8, 3), (3, 5)) == False

def test_weryfikacja_bicia():
    hetmani = [(8, 2), (5, 3), (4, 5), (5, 6), (6, 8)]
    assert weryfikacja_bicia(hetmani, (7, 8)) == [(4, 5), (5, 6), (6, 8)]
    assert weryfikacja_bicia(hetmani, (8, 1)) == [(8, 2), (4, 5)]
    assert weryfikacja_bicia(hetmani, (7, 6)) == [(5, 6)]
    assert weryfikacja_bicia(hetmani, (6, 4)) == [(8, 2), (5, 3), (6, 8)]
    assert weryfikacja_bicia(hetmani, (2, 2)) == [(8, 2)]
    assert weryfikacja_bicia(hetmani, (1, 4)) == []