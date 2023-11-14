# Lekcja 114 - Metody w klasie
# Programowanie obiektowe w Python - definicja klasy - metody

# Czyli mam rozumieć że metoda jest kwadratem, czyli jednocześnie dwoma rzeczami na raz = klasą i metodą? aktualizacja - i funkcją??
# A klasa to po prostu klasa. NO zobaczymy!

# Definicja od ziomeczka:
"""
Wewnątrz definicji klasy można zdefuniować metody, czyli w praktyce funkcje, które są wewnątrz klas.
Metody można wywołać wewnątrz klasy również korzystając z self np. self.get.FullName()


Natomiast w programie odwołujemy się po nazwie obiektu np. person1.get.FullName()
"""

class Person:
    def __init__(self, name, surname, country):
        self.name = name
        self.surname = surname
        self.country = country

# i tutaj zaczynają się METODY:::

    def getFullName(self):
        return ''.join((self.name , " " , self.surname)) # FAJNA CIEKAWOSTKA Z CHATA GPT. JAK ZASTOSUJEMY .JOIN TO ZAMIENIA KROTKE 
#                                                               NA STRINGA. JAK BYM UŻYŁ PLUSÓW ZAMIAST PRZECINKÓW TO NIE TRZEBA
#                                                                   SIĘ W TO BAWIĆ :)
#       return self.name + " " + self.surname - OPCJA BEZ ZABAWY Z '.JOIN'
    
    def printData(self):
        print(self.name, self.surname)

    
person1 = Person('jacek', 'burczymucha', 'pacanowo')
person1.printData()
print(person1.getFullName())

print(person1.name)