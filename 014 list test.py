# Lekcja 14 - Typ List - zadanie
# Zadanie z pętli for i instrukcji do list

numberList =[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("Długość listy 1", len(numberList))
del numberList[3]                               # usuwa 4 pozycje z listy
print("Długość listy 2", len(numberList))



if 9 in numberList:
    print("wartość 9 jest w liście")

for value in numberList:                                 # program wrzuca w zmienną value kolejne elementy listy
    print("To jest wynik value - 5:", value - 5, "value =", value)
   

for value in numberList:
    print("To jest wynik value / 3:", value / 3)   
