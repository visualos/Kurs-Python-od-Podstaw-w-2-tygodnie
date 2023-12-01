# Lekcja 118 - Destruktor

# Specjalna metoda, która ma wykonać jakiś kod, jak coś jest kasowane z pamięci (l o l co za tłumaczenie)

"""
Destruktor to specjalna metoda wywoływana kiedy niszczony jest obieky za pomocą operatora del.
Zanim obiekt będzie skaksonwany z pamięci destruktor daje nam szansę na jeszcze jakieś ostatnie operacje 
np. zamknięcie dostępu do plików itp.
"""


# a dokładnie to działa tak, że Python po jakimś czasie sam usuwa elementy jeżeli z nich nie korzystamy.
# I W TAKIM MOMENCIE, MOŻEMY SIĘ ZABEZPIECZYĆ tym właśnie def __del__(self), i powiedzieć ostatnie słowo przed
# śmiercią np. "print(Zniszczenie obiektu: " + self.getFullName())". No to tyle. 

# A teraz Przykład:
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        print("Object created: " + self.getFullName())

    def getFullName(self):
        return self.name + ' ' + self.surname
    
    def __del__(self):
        print('Zniszczenie obiektu: ' + self.getFullName())



person1 = Person('jacula','mazurkiewicz')
person1.getFullName()


del person1 ## i tutaj odwołujemy się do destruktora. Czyli niszczymy jaculę mazurkiewicz i drukujemy, to co jest w destruktorze
#               czyli: 'Zniszczenie obiektu itd....'

# person1.getFullName() # i tutaj już wlatuje error, bo usunąłem tego ziomeczka