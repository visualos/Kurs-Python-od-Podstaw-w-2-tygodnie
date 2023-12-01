# Lekcja 124 - Dziedziczenie oraz nadpisywanie metod i atrybutów

# OOP - Object-Oriented Programming

# Bardzo ważny temat, bo po jakimś czasie zauważymy że isnieją części wspólne dla metod, klas itd.
# Możemy wtedy stworzyć jedną wspólną klasę, żeby zaoszczędzić miejsca w programie.

# ---- bardzo ważne: 
# class Car(Vehicle) -dziedziczenie klasy. W klasie Car nie ma konstruktora. Patrz poniżej jak to sobie rozpiszemy.


class Vehicle:
    def __init__(self, ):
        self.brand = 'unkknow'
        self.name = 'unkknow'
        self.topSpeed = 100
        self.numWheels = 4

    def printVehicleInfo(self):
        print(self.brand, self.name, self.topSpeed)

    def printData(self): # TA METODA JEST POTRZEBNA DALEJ, PATRZ TAM DALEJ NA DOLE (NADPISYWANIE METOD)
        print('Vehicle info: ', self.brand, self.name) 

class Car(Vehicle):

    def getNames(self):
        self.brand = 'Ford'
        print(self.brand)


    def printCarInfo(self):
        # Klasa 'Car' posiada odziedziczone atrybuty
        
        print('Car brand: ', self.brand)
        print('Car name ', self.name)

        # Też odziedziczone metody z Vehicle
        self.printVehicleInfo()


# DOBRA JESZCZE JEDNO - MOŻEMY NADPISAĆ TAKŻE METODY/ SŁUCHAJ UWAŻNIE ZIOM ---------------- NADPISYWANIE METOD
#
# Można nadpisać również metodę jeżeli odziedziczona nam nie pasuje. Po prostu pisze się ją z tą samą nazwą i nową 
# implementacją. Poniżej metoda printData z Vehicle została zastąpiona nową wersją w Car."""

    def printData(self):
        self.brand = 'Ford'
        self.name = 'Mustang'
        print('Car brand: ', self.brand) ## Nadpisałem metodę. W tym przypadku wyświetlam coś innego niż oryginalna metoda w klasie Vehicle. 
    #                                       Taki jestem kapryśny.
        print('Car name: ', self.name) # I tutaj też zmieniam, a kto mi zabroni.
        


vehicle1 = Vehicle()
vehicle1.printVehicleInfo()

print('nowa linia')
print()



car1 = Car()
car1.printCarInfo()

car1.getNames()
print()

car1.printCarInfo()

# Wydaje się skomplikowane ale takie nie jest. W skrócie:
# - możemy dziedziczyć atrybuty klasy głównej w nowych klasach,
# - możemy zmieniać atrybuty dziedziczonych metod (nadpisywanie metod), tak żeby np. drukowały nam dane tak jak nam się podoba.
# Dodatkowo pamietaj, że funckja __init__(...), wykonuje się automatycznie w dziedziczonej klasie.


