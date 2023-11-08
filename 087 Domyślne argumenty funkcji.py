# Lekcja 87 - Domyślne argumenty funkcji

"""
Funkcje bezargumentowe - nie przyjmują argumentów 
Wywołane są bez przekazanych argumentów.
"""

def printSomething():
    print("Some information")


printSomething()
printSomething()
printSomething()


# Funkcje z argumentami - wymagają prawidłowej kolejności przekazanych argumnetów
# Dodatkowo ilosć przekazanych argumentów musi się zgadzać

def showData(string, number):
    print(string + str(number)) 

"""
Łańcuch "Liczba: " będzie dostępny w funkcji jako zmienna string
Zmienna 10 będzie dostępna w funckcji jako zmienna number
"""

showData("liczba ", 10)

"""
gdy przekażemy dane w złej kolejności
to zwykle skończy się to błędem
"""

#showData(10, "Liczba ") #błąd

"""
-------------------------------------------------------------------
Domyślne argumenty funkcji - 
    Python umożliwia ustalenie wartości domyślnej dla jednego lub więcej argumentów funkcji. 
    Dzięki temu funkcję można wywołać z mniejszą liczbą argumentów 
niż zdefiniowana, a ich wartości zostaną uzupełnione wartościami domyślnymi. W przypadku poniższej
funkcji, pierwszy argument nie ma wartości domyślnej, więc musi być zawsze podawany 
przy wywołaniu funkcji.
"""
def printUser(name, country = "unknown", email = "default@example.com"):
    print( "User " + name + " from country: " + country + " and email" + email)
 # automatycznie wyświetli coutry jako unknown

"""
 Nazwane argumenty w funkcji - 
 Funkcje można wywoływać z argumentami nazwanymi, co pozwala na przekazywanie danych do 
 funkcji bez konieczności zachowania okreslonej kolejności.
 Argument nazwany przekazuje się jako parę: argument = wartość
 Jak widać poniżej argumenty nazwane mogą byż przesyłane w dowolnej kolejności.
 """

def showData(string, number):
    print(string + str(number))


print("NAZWANE ARGUMENTY FUNKCJI")
showData(string = "Liczba", number = 10)
showData(number = 10, string = "Liczba")



"""
Domyślne argumenty funkcji i nazwane elementy funkcji można z powodzeniem ze sobą łączyć.
"""

def function(kupa, sikuLitry = "unknown", email = "default@expamlpe.com"):
    print(kupa, sikuLitry, email)

function(kupa = "duża")







