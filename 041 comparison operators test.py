# Lekcja 41 - Operatory porównania - zadanie

"""
Zadanie - operacje z operatorami porównania
1) Stwórz dwie zmienne: age1 i age2, przypisz im wartości 25 i 30
2) Sprawdź, czy age1 jest mniejsze od age2, wyświetl wynik
3) Sprawdź, czy age1 jest równe od age2, wyświetl wynik
4) Sprawdź, czy age1 jest większe od age2, wyświetl wynik
5) Sprawdź, czy age1 jest różne od age2, wyświetl wynik
6) Dodaj do age1 10 lat i sprawdź, czy teraz age1 jest większe bądź równe age2, wyświetl wynik
7) Odejmij od age2 5 lat i sprawdź, czy teraz age1 jest mniejsze bądź równe age2, wyświetl wynik
"""
#1
age1 = 25
age2 = 30
#2
print(age1 < age2)
#3
print(age1 == age2)
#4
print(age1 > age2)
#5
print(age1 != age2)
#6
age1 += 10
print(age1 >= age2)
#7
age2 -= 5
print(age1 <= age2)