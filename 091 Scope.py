# Lekcja 91 -Scope

"""
Scope, czyli nic innego jak zasięg zmiennych w Pythonie. Dzielimy zmienne na lokalne i globalne.
Lokalna, to taka tylko w funkcji, a globalna to taka co jest dostępna wszędzie.

Dostęp do zmiennych lokalnych jest tylko lokalny, kumasz.
"""
number = 20
def localVariable ():
    print(number) # zmienna globalna
    string = "test" # zmienna lokalna
    print(string)

localVariable()

# brak dostępu do funkcji, bo string jest lokalny:
"""
print(string) 
"""


def localVariable ():
   
    global number # wskazuje na zmienną globalną
    print(number)

localVariable()
