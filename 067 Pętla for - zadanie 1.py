# Lekcja 67 - zadanie 1 

"""
Liczby nieparzyste dodane do set
1) Dodaj listę numList z wartościami od -3 do 5 z krokiem co 1
2) Dodaj set z wartością początkową -2
3) Stwórz pętlę for in przechodzącą po numList
4) W każdej iteracji pętli sprawdź czy liczba z listy jest nieparzysta,
    czyli reszta z dzielenia przez dwa nie może być równa zero (!=0).
    Dodaj nieparzystą liczbę do zestwu używając metody add() na set
5) Wyświetl w konsoli nieparzyste liczby w set z pomocą pętli for
"""


numList = [ -3, -2,-1,-0,1,2,3,4,5]
set = {-2}
print("wartość set", set)

for value in numList:
    if int(value) % 2 != 0:
        set.add(value)
for value in set:
    print(value)     
  