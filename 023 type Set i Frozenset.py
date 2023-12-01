# Lekcja 23 - Typ Set i Frozenset - ćwiczenie

numberSet = {2, 3, 1, 4, 5}
numberSet.add(22) # można wpisać tylko jedną liczbę 
numberSet.add(50)
numberSet.add(5) # nie doda drugiej piątki
numberSet.add(2233)
numberSet.add(212)
print(numberSet)

numberSet.discard(1) # usunięcie jedynki z zestawu
print(numberSet)       

print(type(numberSet)) # <class 'set'>

for value in numberSet: # zwykła iteracja po wartościach zestawu
    print(value)

frozenSetNumbers = frozenset(numberSet) # tworzenie zestawu typu frozenset
print(type(frozenSetNumbers)) # <class 'frozenset'>