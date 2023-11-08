# Lekcja 28 - Konwersje typów tuple, list, dict, set, frozenset


listData = [1, 2, 3, 4]
tupleData = tuple(listData) #konwersja na krotkę
print(listData)


tuple = {"Ola", "Adam"}
list2 = list(tuple)
print(list2)

numberList = [4, 6, 8, 9, 10, 11, 12]
uniqueSet = set(numberList) # zmiana na zbiór set

print(type(uniqueSet))
print(uniqueSet)

# Konwersja na słownik

contactTuples = (("Bob", "bob@sample.com"), ("Eva", "eva@sample.com"))
contactDict = dict(contactTuples)
print(type(contactDict))
print(contactDict)
print(contactDict["Eva"])
