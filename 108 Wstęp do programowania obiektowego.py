# Lekcja 108 - Wstęp do programowania obiektowego

"""
Programowanie obiektowe w Python
Python od momentu powstania jest językiem obiektowym, włościwie wszystko w Pytjon
jest obiektem. Wartozadać pytanie czym tak naprawdę jest programowanie obiektowe?

Do tej pory operowaliśmy na danych za pomocą programowania proceduralnego czyli w praktyce
funkcji do których byłyprzekazywane dane w postaci zmiennyvh, mogły również zwracać jakieś wartości.
Każdy roblem jest podzielony na etapy i na wywowływanie funkcji.

Programowanie obiektowe patrzy szerzej na rozwiązywanie problemów grupując funkcje oraz dane, króre te funkcje obsługują 
w jedną całość czyli obiekty. Znacząco to ułatwia programowanie. wręcz jest niezbędne podczas tworzenia rozbudowanych programów.



"""
# konstruktor, specjalna metoda inicjująca obiekt.
# Jest wywołany podczas utworzenia instrancji obiektu
# self to pierwszy parametr zawsze mający obiekt
# na rzecz którego wywołana kest metoda

class Car:
    def __init__(self2, brand, model, year): # wpisałem self 2 żeby sprawdzić czy działa tak samo jak self bez liczby i działa :)
        self2.carName = brand + " " + model
        self2.productionDate = year

# metoda printInfo otrzymuje tylko jeden
# obowiązkowy parametr self czyli obiekt
# na którym jest wywołana metoda

    def printInfo(self2):
        print( self2.carName + " " + str(self2.productionDate))


 # k;asa Car używana jest jako szablon 
 # # do powołania dowolnej
 # # ilości obiektów na jej podstawie
 # poniżej dwa obiekty klasy Car
 #


mustang = Car("Ford", "Mustang", 1970)
mustang.printInfo()   

viper = Car("Dodge", "Viper", 1997)
viper.printInfo()