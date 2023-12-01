# Lekcja 120 - Statyczna zmienna.py


"""
OOP w Python - statyczna zmienna wspólna dla wszystkich obiektów
"""

"""
Zmienną statyczną tworzymy wewnątrz klasy, poza konstruktorem i metodą. Ciekawą właściwością takiej statycznej zmiennej
jest fakt, że jest tylko jedną i jedyną dla wszystkich instancji obiektu na bazie danej klasy.

W przykładzie zmienną statyczną jest numEmployees zdefuniowana na poziomie klasy. Dostęp do niej uzyskuje się poprzez nazwę
klasy i nazwę zmiennej statycznej.
"""

# na moje oko to wszystkie zmienne, które tworzymy od razu pod klasą. Od razu, na samej górze. Patrz na dole
class Employee:
    numEmployess = 0 # o tutaj!



# no i teraz moimi słowami. Na dole przykład jak odwołać się do zmiennej statycznej (numEmployess) w kodzie:

    def __init__(self, name):
        self.name = name # atrybut obiektu
        print('self.name: ', self.name)

        # zwiększanie  wartości statycznej zmiennej wspólnej:
        Employee.numEmployess += 1
        print('Employee.numEmployess', Employee.numEmployess)

employee1 = Employee('radek')
employee2 = Employee('jacek')



