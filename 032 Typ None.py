# Lekcja 32 - Typ None czyli brak wartości
"""
Typ None
Oznacza brak wartości, np. że zmienna nie posiada przypisanej wartości, 
coś jak null w innych językach programowania.
"""

data = None
print(type(data)) # <class 'NoneType'>
if data is True:
    print("Data is true")
elif data is False:
    print("Data is False")
else:
    print("None is None")

"""
Typ None pozwala zaoszczędzić miejsce w zaawansowanym etapie tworzenia programu
gdy nie potrzebujemy już jakiejś zmiennej.
"""
