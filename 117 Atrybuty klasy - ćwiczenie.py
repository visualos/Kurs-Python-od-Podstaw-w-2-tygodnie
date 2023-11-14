# Lekcja 117 - Atrybuty klasy - ćwiczenie

class Student:
    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.schoolName = None
        self.fieldOfStudy = None

    def printInfo(self):
        print(self.name, self.surname, self.age, self.city, self.schoolName, self.fieldOfStudy)

student1 = Student("Kasia", 'Brzęćzyszczykiewicz', 21, 'Kraków')
student1.printInfo()

student1.city = "Warszawa"
student1.printInfo()

class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.studentList = []
        self.fieldOfStudy = ['IT', 'Math', 'Robotics']

    def addStudent(self, student):
        if isinstance(student, Student):  # Tutaj zwraca True albo False. Czyli czy student jest instancją klasy Student
            self.studentList = student
            student.schoolName = self.name

    