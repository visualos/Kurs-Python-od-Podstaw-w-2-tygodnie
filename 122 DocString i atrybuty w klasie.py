# Lekcja 122 - DocString i atrybuty w klasie

# OOP w Python - definicja klasy - string dokumentujący

"""
String dokumentujący to łańcuch znaków w pierwszej linijce definicji funkcji, metody czy klasy.
Może być pobrany za pomocą nazwy klasy oraz atrybutu __doc__

Takie łańcuchy znaków stanowią opis działania danej funkcjonalnosći większej częsci kodu np. klasy, modułu itd. Nie należy mylić tych
informacji z komentarzami, które opisują konkretny kod np. jak działa.
"""

# Dobra. Na moje DocString to jest komentarz w wersji premium. Zapisujemy go w pojedynczych nawiasach

class Person:
    'String do dokumentacji: klasa Person opisująca osobę' # to jest to!!!! O tym się mówi w tej lekcji
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.printDocString()
        


    def printDocString(self):
        print( Person.__doc__, self.name, self.surname) # funkcja Person.__doc__.... - wywołuje ten komentarz premium z początku (DocString)
        print('nazwa klasy: ', Person.__name__) # dodatkowa fajna opcja. Wypisuje nazwę klasy
        print('tutaj funkcja module wypisuje nazwę modułu (tutaj akurat __main__), w którym zdefiniowana jest klasa: ', Person.__module__)
person1 = Person('Jacek', 'Burczymucha')
person2 = Person('Jacek2', 'Burczymucha2')