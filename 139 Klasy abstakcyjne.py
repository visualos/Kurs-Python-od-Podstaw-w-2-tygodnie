# Lekcja 139 - Klasy abstakcyjne.py

'''
Klasa abstrakcyjna w Pythonie to klasa, która zawiera jedną lub więcej metod abstrakcyjnych, czyli metod bez implementacji. 
Metody te służą jako "szkielet" dla klas dziedziczących po klasie abstrakcyjnej. Klasy abstrakcyjne same w sobie nie mogą być 
instancjonowane, co oznacza, że nie można tworzyć obiektów bezpośrednio z klasy abstrakcyjnej.

Idea klasy abstrakcyjnej polega na dostarczeniu interfejsu lub szablonu dla klas dziedziczących. Oznacza to, że klasy dziedziczące 
muszą dostarczyć implementację wszystkich metod abstrakcyjnych zdefiniowanych w klasie abstrakcyjnej, w przeciwnym razie nie będą 
mogły być instancjonowane same w sobie.

W Pythonie moduł abc (Abstract Base Classes) dostarcza mechanizm klasy abstrakcyjnej za pomocą dekoratorów lub dziedziczenia 
z klasy ABC. Przykładowo:
'''
# Instrukcja from abc import ABC w Pythonie oznacza importowanie klasy ABC z modułu abc, który jest częścią standardowej 
# biblioteki Pythona:
from abc import ABC, abstractmethod

'''
W Pythonie moduł abc (Abstract Base Classes) zawiera narzędzia do definiowania klas abstrakcyjnych i metod abstrakcyjnych. 
Klasa ABC jest częścią tego modułu i służy jako klasa bazowa dla klas abstrakcyjnych. Umożliwia definiowanie klas abstrakcyjnych 
poprzez dziedziczenie z niej oraz dekoratorów abstractmethod do oznaczania metod jako abstrakcyjne.
'''

class Animal(ABC):  # Klasa abstrakcyjna Animal
    @abstractmethod # dekorator który informuje Pythona, że to jest nasza abstrakcyjna metoda
    def make_sound(self):
        pass

class Dog(Animal):  # Klasa dziedzicząca po Animal
    def make_sound(self):
        return "Woof!"

class Cat(Animal):  # Klasa dziedzicząca po Animal
    def make_sound(self):
        return "Meow!"

# animal = Animal()  # Nie można utworzyć instancji klasy abstrakcyjnej
dog = Dog()
print(dog.make_sound())  # Wywołanie metody zdefiniowanej w klasie dziedziczącej


"""
Klasa abstrakcyjna Animal definiuje metodę abstrakcyjną make_sound(), która musi być zaimplementowana w klasach dziedziczących. 
Klasy dziedziczące Dog i Cat implementują tę metodę, co pozwala na tworzenie obiektów tych klas i wywoływanie ich metod. 
Klasy dziedziczące muszą zastosować implementację metod zdefiniowanych w klasie abstrakcyjnej, aby być kompletnymi i użytecznymi.
"""