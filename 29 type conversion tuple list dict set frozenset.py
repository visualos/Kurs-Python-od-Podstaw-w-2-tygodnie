# Lekcja 28 - Konwersje typów tuple, list, dict, set, frozenset

numberList = [7, 8, 9, 10, 11, 12]
tupleData = tuple(numberList)       # zmiana listy na krotkę
print(tupleData)                    # (7, 8, 9, 10, 11, 12) w nawiasach okrągłych, bo to tuple
print(type(tupleData))              # <class 'tuple'>

list = list(("Ewa", 12, 15))        # zmiana krotki na listę
print(list)                         # ['Ewa', 12, 15] - w nawiasach kwadratowych, bo to lista
print(type(list))                   # <class 'list'>

setData = set((1, 1, 2, 3, 4, 4, 5, 6)) # zmiana krotki na zbiór
print(setData)                          # {1, 2, 3, 4, 5, 6}, klamry, bo to zbiór. Liczby już się nie powtarzają.
print(type(setData))                    # <class 'set'>

frSet = frozenset(setData)              # mrożenie zbioru na frozenset
print(frSet)                            # frozenset({1, 2, 3, 4, 5, 6}), klamry + nawiasy bo zamrożony   
print(type(frSet))                      # <class 'frozenset'>   

contactsTuple = (("Ola", "ola@email.com"),("Ania", "ania@email.com") )  # tworzenie krotki odpowiedniej pod słownik
contactsDict = dict(contactsTuple)                                      # krotka na słownik
print(type(contactsDict))                                               # <class 'dict'>
print(contactsDict)                                                     # {'Ola': 'ola@email.com', 'Ania': 'ania@email.com'}



