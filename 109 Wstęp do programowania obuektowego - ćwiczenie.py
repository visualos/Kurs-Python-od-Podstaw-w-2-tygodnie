class Vehicle:
    def __init__(self, brand, model, color, year, distanceTravelled):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.distanceTravelled = distanceTravelled
        self.maxSpeed = None  # Initialize maxSpeed attribute
        self.displayInfo()

    def displayInfo(self):
        print(self.brand, self.model, self.color, self.year, self.distanceTravelled)

    def setMaxSpeed(self, newMaxSpeed):
        self.maxSpeed = newMaxSpeed

opel = Vehicle("Opel", "Zafira", "blue", 2001, 1)
opel.distanceTravelled = 1000
opel.setMaxSpeed(145)