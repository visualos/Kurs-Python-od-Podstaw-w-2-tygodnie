# Lekcja 128 - Hermetyzacja w klasie

# OOP w Python - hermetyzacja / enkapsulacja - metody i zmienne będą prywatne jeśli mają przedrostek z podwójnym podkreśleniem, są
# z podwójnym podkreśleniem, są tylko dostępne w obiekcie na bazie tej klasy

# Zamieniłem przykład ziomeczka z Udemy na chatagpt. Jest bardziej zrozumiały.
# Oto on:


# I to jedyny najprostszy przykład, który powinien być użyty.
class Car:
    def __init__(self, brand, model):
        self._brand = brand  # Zmienna chroniona (convention-based)
        self.__model = model  # Prywatna zmienna (name mangling)

    def get_model(self):
        return self.__model

# Użycie klasy Car
car = Car("Ford", "Mustang")
print(car._brand)  # Dostęp do zmiennej chronionej (niezalecane)
# print(car.__model)  # To spowoduje błąd, ponieważ jest to zmienna prywatna
print(car.get_model())  # Prawidłowe uzyskanie wartości zmiennej prywatnej przez publiczną metodę


"""
A teraz moimi słowami. Hermetyzacja w klasie polega na tym, że blokujemy niektóre zmienne lub metody. 
Robimy to za pomocą dodania dwóch podkreślników __ na początku nazwy zmiennej lub metody. Stosuje się ją NIE PO TO, ŻEBY INNI 
PROGRAMIŚCI NIE MIELI DOSTĘPU DO NASZYCH FUNKCJI, ALE PO TO ŻEBY ZAZNACZYĆ ŻE TA ZMIENNA/METODA MA BYĆ PRYWATNA.

TO POMAGA W PÓŹNIEJSZYM ZARZĄDZANIEM KODEM!!! 

TWORZY WYRAŹNĄ STRUKTURĘ I ZAPOBIEGA BŁĘDOM!!!

CHUJ NIE PORADNIK


"""