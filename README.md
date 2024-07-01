## Hetmani i pionek

### Uwagi:
- Hetman porusza się pionowo, poziomo lub ukośnie,
- Maksymalna liczba hetmanów (k) to 5.


### Program generuje planszę 8 x 8. W skład mapy wchodzi:
- k liczba hetmanów rozmieszczonych losowo na mapie,
- jeden pionek rozmieszczony losowo na mapie.

Każdy z elementów zostaje ustawiony na różnej od siebie pozycji.
Po włączeniu programu schemat planszy wyświetla się dla użytkownika.

Program po wyświetleniu mapy odpowiada na pytanie:
_Czy pionek zostanie zbity przez któregoś z hetmanów?_

Użytkownik otrzymuje również informacje na jakich pozycjach znajdują się hetmani, 
którzy mają możliwość zbicia pionka (o ile tacy istnieją).

Po tym komunikacie użytkownik programu ma możliwość:
- wylosowania nowej pozycji dla pionka z pozostawieniem pierwotnego układu hetmanów,
- usunięcia dowolnego hetmana (za pomocą wskazanie jego pozycji),
- ponownej weryfikacji bicia po ustaleniu zmian,
- wyjścia z programu.

#### W pliku test_szachy.py przygotowane zostały przykładowe pytest'y.