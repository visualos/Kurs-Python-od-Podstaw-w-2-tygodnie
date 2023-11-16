# Lekcja 132 - Moduły w Python.py

# Po mojemu: po prostu plik.py, import innych funkcji, metod, klas itd. :) Bardzo fajna rzecz


"""
# Moduły - instrukcja import
# Im więcej kodu piszemy tym bardziej rośnie potrzeba modularyzacji i organizacji naszego programu, aby 
# łatwiej było kontrolować i odnaleźć się w kodzie źródłowym. Przykładowo każda z klas może być w odzielnym pliku,
# a dopiero główny plik importujący poszczególne klasy wykorzysta je w faktycznym programie. Dodatkowo pliki z klasami 
# mogą być użyte w innych programach co oszczędza nam czas.

Moduł to plik Python, który może mieć funkcje, klasy, zmienne czy korzystający z nich działający kod.

Instrukcja import importuje jako moduł dowolny kod z innego pliku. Funkcja addNumbers w mathModule.py jest zaimportowana
do moduleTest.py i użyta jako mathModule.addNumbers(3,8)
"""

# funkcje w osobnym pliku _132mathModule.py:
"""def addNumbers(a, b):
    return a + b 
"""

# a to plik moduleTest.py:
import _132mathModule
print(_132mathModule.addNumbers(3, 8))

# Dodatkowo możemy importować wielu modułów po przecinku za jednym razem np:
# import mathModule, random

# Dodatkowo możemy skorzystać ze słówka 'from'
#from User (nazwa pliku User.py) import User(nazwa klasy), Employee(nazwa II klasy)





