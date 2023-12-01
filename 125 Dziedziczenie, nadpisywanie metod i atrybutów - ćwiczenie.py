# Lekcja 125 - Dziedziczenie, nadpisywanie metod i atrybutów - ćwiczenie


class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.topSpeed = 140
        self.numWheels = 4

    def printVehicleInfo(self):
        print('Brand: ', self.brand, 'name: ', self.name, 'topSpeed: ', self.topSpeed, 'numWheels: ', self.numWheels)


vehicle1 = Vehicle('opel', 'Zafira')
vehicle1.printVehicleInfo()

class Car(Vehicle):
    def printCarInfo(self):
        self.topSpeed = 170
        print('to jest print z klasy dziedziczonej')

car1 = Car('Peugeot', '206')
car1.printCarInfo()
car1.printVehicleInfo()


# W tej lekcji powtórzyłem to co było na ostatniej. Czyli jak dziedziczyć klasy oraz jak nadpisywać metody w dziedziczonej klasie. :)