# Lekcja 126 - Dziedziczenie a konstruktory

# W poprzednich przykładach pomijany był konstruktor w nowej klasie. Był on po prostu kopiowany z klasy bazowej.

# A teraz pewnie będziemy tworzyć nowy konstruktor dla nowej klasy. Lecimy!

class Person:
    def __init__(self, name):
        self.name = name
        print('To jest drukowane w konstruktorze klasy bazowej')


class Employee(Person):
    def __init__(self, name):

# TWORZENIE NOWEGO KONSTRUKTORA        
       self.name = name
       print('To jest drukowane w konstruktorze klasy dziedziczonej (pochodnej)')

# WYWOŁANIE NADRZĘDNEGO KONSTRUKTORA  - Dodatkowo
#       Person.__init__(self, name)
    """    # Wywołanie nadrzędnego konstruktora można pominąć. To jest tylko wtedy jak chcemy się odwołać do konstruktora klasy bazowej.
        # A to jest dziwne. Bo jak ominiemy wszystko, to przecież konstruktor bazowy sam się skopiuje hmm...
        dobra już wiem. Ponowne wywołanie kontruktora bazowego jest wtedy kiedy nie potrzebuje wszystkich tych rzeczy w nawiasach.
        np. potrzebuje tylko imię, albo tylko nazwisko itd.

        Dzięki temu nie muszę przypisywać wartości dla wszystkich atrybutów fuck yea.
        )   """ 
#       self.name = name
#       print('To jest drukowane z oryginalnego konstruktora, powołanego w klasie pochodnej. uff')

person1 = Person('Europa')
employee1 = Employee('Jacek Mazurkiewicz')

