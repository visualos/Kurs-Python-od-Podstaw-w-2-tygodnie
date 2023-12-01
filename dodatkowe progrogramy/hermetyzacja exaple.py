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
