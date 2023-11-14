# Lekcja - 116 Atrybuty klasy

"""
Programowanie obiektowe w Python - definicja klasy - atrybuty czyli zmienne klasy
"""

# Ja mam takie wrażenie, że tutaj chodzi o to co znajduje się w nawiasach przy tworzeniu głównej klasy np. Person

"""
Dane wewnąrz obiektu możemy nie tylko odczytać ale również je zmienić wpisując po kropce (dot operator)
nazwę zmiennej / atrybutu i następnie po znaku równości nową wartość.

person1.name = 'Kasia' # nadpisanie
person.city = 'Warszawa'
"""
# Jeżeli nie ma atrybutu to zostanie dodana nowa z odpowiednią wartością do obiektu, czyli dane mogą być dodawane
# dynamicznie! Nie trzeba ich definiować w definicji klasy.

class Person:
    def __init__(self, name, surname, country):
        self.name = name
        self.surname = surname 
        self.country = country

    def getFullName(self):
        return self.name + ' ' + self.surname
    
    def printData(self):
        print(self.name, self.surname, self.country)

person1 = Person('Ola', "Brzęczyszczykiewicz", "Polska")
person1.printData()
person1.name = 'Kasia'

person1.printData()