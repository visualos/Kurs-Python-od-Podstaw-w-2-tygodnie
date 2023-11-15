# Lekcja 127 - Dziedziczenie i konstruktory - zadanie

class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city
        print('Person constructor! ')

    def printPersonData(self):
        print('Tutaj drukujemy dane z klasy głównej', self.name, self.surname, self.city)


person1 = Person('Jacek', 'Mazurkiewicz', 'Warszawa')
person1.printPersonData()

class Student(Person):
    """def __init__(self, name):
        self.name = name
        print('Tutaj drukuje się klasa Student czyli klasa pochodna')"""
    
    def __init__(self, name, surname, city, companyName, salary):
        Person.__init__(self, name, surname, city)
        self.companyName = companyName
        self.salary = salary

    def printStudentName(self):
        print('Tutaj drukuje się nazwa Studenta: ', self.name, self.salary)

student1 = Student('Radek', 'Brzęczyszczykiewicz', 'Warszawa', 'Google', '20000$')
student1.printStudentName()
student1.printPersonData()


class Worker(Person):
    def __init__(self, name, surname, city, departament):
        Person.__init__(self, name, surname, city)
        self.departament = departament

worker1 = Worker('Stefan', 'Sprzątacz', 'Warszawa', 'sprzątanie piwnicy')
worker1.printPersonData()        