# Lekcja 111 - Definicja klasy

#Odtwarzam program ziomeczka z pamięci:

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def getFullName(self):
        return 'Imieczko ' + self.name + ', Nazwiseczko: ' + self.surname + ', wiek: ' + str(self.age)


    def displayPerson(self):
        print('Imię '+ self.name + ', Nazwisko: '+ self.surname + ', wiek: '+ str(self.age))
        

person = Person('Radek', 'Męczybuła', 14)
person.displayPerson()

print(person.getFullName())
