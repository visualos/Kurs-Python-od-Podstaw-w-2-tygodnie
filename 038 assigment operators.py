# Lekcja 38 - Operatory przypisania - zadanie

"""
Zadanie - operacje na rachunku bankowym, skorzystaj ze skóconych
operatorów przypisania z operacją matematyczną np: += -= *= /= itp.

Uwaga, po każdej operacji wyświetl saldo w konsoli
1) Stwórz zmienną accountBalance z wartośćią początkową 1400
2) Dodaj wartość nowej pensji 7000
3) Odejmij 2300 kosztów na mieszkanie
4) Błąd banku pomnożył Twoje saldo czterokrotnie
5) Odejmij 4000 na samochód
6) Bank zorientował się, że powstał błąd i coda ostatnie transakcje. Dodaj do salda 4000, podziel je przez 4
i dopiero teraz odejmij 4000.
7) Pokaż saldo końcowe.
"""

accountBalance = 1400
accountBalance += 7000
accountBalance -= 2300
accountBalance *= 4
accountBalance -= 4000
accountBalance = ((accountBalance + 4000)/4) - 4000

print(accountBalance)