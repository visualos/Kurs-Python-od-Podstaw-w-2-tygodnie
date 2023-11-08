# Lekcja 71 - Pętla for z range - ćwiczenie
"""
Zadanie: Sumowanie liczb z pomocą pętli for i range
Wymagania:
1) Stwórz zmienną total, która będzie miała ustawioną wartość 0 przed każdą pętlą
2) Zrób pętlę for z wartościami od 0 do 200 z range, zsumuj liczby i wyświetl rezultat w konsoli
3) Zrób pętlę for z range z liczbami od 50 do 100, dodaj je i wyświetl wynik
4) Zrób kolejną pętlę z range od 0 do 300 z krokiem co 3, dodaj liczby i wyświetl wynik w konsoli
"""

total = 0
for v in range(201):
    total += v
print(total)

total = 0
for v in range(50, 101, 1):
    total += v
print(total)

total = 0
for v in range(0, 301, 3):
    total += v
print(total)