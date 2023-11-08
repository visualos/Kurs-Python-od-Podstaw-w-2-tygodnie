"""
Lekcja 22 - Typ Set i Frozenset - zbiór unikalnych wartości

set - "zestaw", to zbiór nieuporządkowanych, unikalnych wartości
Zbiór w Pythonie nie pozwala na dodawanie zduplikowanych elementów, jest iterowalny,
modyfikowalny, ale nie ma indeksów dla elementów. Istnieje wariant tego obiektu, zwany
frozenset, który jest niemodyfikowalny. Zbiory są zapisywane za pomocą nawiasów 
klamrowych i oddzielonych przecinkami wartości.

"""

numberSet = {0, 4, 8, 12, 16} # Inicjalizacja zbioru
print(numberSet)

numberSet.add(20) # Dodanie elementu do zbioru. Działa tylko raz. Dodanie tej samej wartości będzie ignorowane.
print(numberSet)

numberSet.discard(8) # Usunięcie wartości 8 ze zbioru
print(numberSet) 

for value in numberSet: # iteracja po elementach zbioru
    print(value)
"""
Frozenset - niemutowalny zestaw, to nieuporzadkowany zbiór unikalnych wartości.
Frozentset jest podobny do zbioru, ale różni się tym, że po utworzeniu nie można go modyfikować.
"""
exampleSet = {2, 6, 10, 14, 18}             # Inicjacja zbioru
frozenExapmleSet = frozenset(exampleSet)    # Tworzenie niemodyfikowalnego zbioru
frozenExapmleSet.add(30)                    # nie działa, błąd. Nie można dodać wartości do frozenset

