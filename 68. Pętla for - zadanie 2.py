# Lekcja 68 - Petla for - zadanie 2

"""
1) Stwórz listę o nazwie numList z wartościami od -5 do 3 z krokiem co 1
2) Dodaj do listy dodatkowe elementy: 1, 2, 3, 4 z metodą append()
3) Utwórz set o nazwie tripledSet z wartością początkową -6
4) Stwórz pętlę for in z listą numList
5) W każdej iteracji pętli dodaj liczbę z listy pomnożoną przez 3 do set.
6) Wyświetl w konsoli liczby z tripledSet z pomocą pętli for.
"""

numList = [-5,-4,-3,-2,-1,0,1,2,3]
print(numList)
numList.append(1)
numList.append(2)
numList.append(3)
numList.append(4)
print(numList)

tripledSet = {-6}

for value in numList:
    tripledSet.add(value*3)
for value in tripledSet:
    print(value)