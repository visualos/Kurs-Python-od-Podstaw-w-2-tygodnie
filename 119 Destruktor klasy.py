# Lekcja 119 - Destruktor klasy

class Dog:
    def __init__(self):
        print('To jest przykładowy konstruktor, żeby póżniej użyć destruktora dla przykładu')

    def __del__(self):
        print('Destruktor')

dog1 = Dog()
# i destruktor wykonuje się automatycznie na koniec programu. CIEKAWE!/ nie muszę wywoływać destruktora, sam się jebaniec wowołał
# na końcu