# Lekcja 130 - Gettery i settery.py


# Gettery i settery to metody które pobierają i ustawiają jakąś zmienną.
# ziomek nazywa je 
# @property - dekorator
# getter pobiera wartość 
# i @gears.setter # setter ustawia wartość

class Vehicle():
    def __init__(self):
        self.__gears = -5
    

    @property
    def gears(self):
        if(self.__gears > 0):
            return self.__gears
        else:
            return -1
        
    @gears.setter
    def gears(self, gears):
        if(gears > 0 ): self.__gears = gears

    def printGears(self):
        print("Gears: ", self.__gears)

vehicle1 = Vehicle()
vehicle1.printGears()
vehicle1.gears


# Ogólnie rzecz biorąc, chatGPT mówi że używanie getera (@property) wpływa na czytelność kodu i w sumie nic poza tym.
# Pierdoli coś o dodawaniu logiki, ale zwykła metoda też może używać logiki. Jedyną różnicą jest fakt, że później mamy
# łatwiejszy dostęp do wyniku operacji (jeśli zastosujemy getter). Zamiast pisać vehicle1.gears() możemy napisaź vehicle1.gears.

# Myślę, że zalet gettera jest znacznie więcej ale to wyjdzie w praniu, przy tworzeniu projektów.

"""

Wyplute przez chataGPT:
Używanie dekoratora @property umożliwia tworzenie właściwości (properties) w klasach, 
co przypomina dostęp do atrybutów, a jednocześnie daje większą kontrolę nad zachowaniem danych. 
Ta nazwa została przyjęta, aby podkreślić tę funkcjonalność - tworzenie specjalnych cech (properties) obiektów.


MOJE PYTANIE: Czyli mogę zdefiniować setter za pomocą @ property?
ODPOWIEDŹ:
Tak, właśnie tak działa dekorator @property w Pythonie -
umożliwia on zarówno definiowanie gettera, jak i settera dla atrybutu klasy.
Aby zdefiniować setter za pomocą dekoratora @property, należy po getterze wykorzystać dodatkowy dekorator 
o nazwie nazwa_atrybutu.setter. Oto przykład:
"""