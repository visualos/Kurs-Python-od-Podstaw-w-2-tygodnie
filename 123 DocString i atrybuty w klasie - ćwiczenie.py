# Lekcja 123 - DocString i atrybuty w klasie - ćwiczenie


# kodzik skopiowałem sobie elegancko od ziomeczka z Udemy
# i lecimy z tematem


class Employee: 
    "Employee class describing company employee" # string dokumentujący (DocString)
    # static variables for all objects based on Employee
    numEmployees = 0
    employeesList = []

    def __init__(self, name):
        "Constructor for Employee" # kolejny DocString
        """
            line 1
            line 2
        """
        self.name = name

        Employee.numEmployees += 1
        print(self.name, "numEmployees: ", Employee.numEmployees)

        Employee.employeesList.append(self)

    
    def printAllEmployees(self):
        for el in Employee.employeesList:
            print(el.name)
print(' ZACZYNAMY DRUKOWANKO')

employee1 = Employee("Ola")
employee2 = Employee("Kasia")
employee3 = Employee("Adam")
employee4 = Employee("Karol")

print("Employee.numEmployees: ", Employee.numEmployees)
print()


print('ZACZYNAMY DRUKOWANKO NUMER 2')
employee1.printAllEmployees()
print()
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print()
# teraz ziomek robi coś i zamiast tłumaczyć to dyktuje kod. Także lecę razem z nim:

# DEFINICJA Z CHATA GPT DO LINIJKI PONIŻEJ:
#
# Ta funkcja sprawdza, czy obiekt employee1 posiada atrybut o nazwie 'name'. 
# Metoda hasattr() jest wbudowaną funkcją w języku Python, 
# która zwraca wartość logiczną True lub False 
# w zależności od tego, czy określony atrybut istnieje w danym obiekcie.
print("name attr in Employee: ", hasattr(employee1, "name") )
print("city attr in Employee: ", hasattr(employee1, "city") )
employee1.city = "Krk"
print("city attr in Employee: ", hasattr(employee1, "city") ) 

# ZNOWU ZIOMECZEK DYKTUJE KOD. JAK NA STUDIACH LOL. DOBRA TO JEST TA LINIJKA:

 

# Funkcja setattr() w języku Python służy do ustawiania wartości atrybutu dla określonego obiektu. 
# W konkretnym przypadku:
setattr(employee1, "name", "Kasia") 
employee1.name  = 'JACULAAA' # to samo co na górze


#Ten kod wypisuje wartość atrybutu "name" obiektu employee1 za pomocą funkcji getattr().
# Funkcja getattr() w języku Python służy do pobierania wartości określonego atrybutu z danego obiektu.
# W przypadku podanego kodu:
print("employee1.name: ", getattr(employee1, "name") ) # to się przydaje gdy mamy nazwę zmiennej w innej zmiennej. Jeśli nie to wystarczy napisać
#                                                        pritn(employee1.name)
print(employee1.name)

print('Użycie metody help()')
#help(Employee)
 

