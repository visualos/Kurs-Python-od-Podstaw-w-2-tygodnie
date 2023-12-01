# Lekcja 13 - Petla for do przęglądania zawartości listy

myList = [1, 2, 3, "Marta", "Adam", 34] # tworzy listę

print(myList)                           # [1, 2, 3, 'Marta', 'Adam', 34]
print(type(myList))                     # <class 'list'>
print(myList[2])                        # drukuje 3 (bo to 2 indeks z listy)


for radej in myList:        # radej to nowa zmienna tworzona w celu iteracji
   print(radej*3)  # drukuje wszystko pomnożone przez 3, wyrazy potraja