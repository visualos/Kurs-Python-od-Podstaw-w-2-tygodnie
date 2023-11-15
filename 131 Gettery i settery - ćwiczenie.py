# Lekcja 131 - Gettery i settery - ćwiczenie


class Vehicle:
    def __init__(self):
        pass

    @property
    def gears(self):
        print("getter:", self.__gears)
        if(self.__gears > 0):
            return self.__gears
        else:
            return -1

    @gears.setter
    def gears(self, newGears):
        print("newGears:", newGears)
        if(newGears > 0): self.__gears = newGears


vehicle1 = Vehicle()
vehicle1.gears = 12
print(vehicle1.gears)


# Python, pomimo tego że setter jest poniżej gettera, wie że występują oba. I wie, że chcemy ustawić jakąś nową wartość dla 
# vehicle1. Dlatego najpierw drukuje to co jest w setterze.