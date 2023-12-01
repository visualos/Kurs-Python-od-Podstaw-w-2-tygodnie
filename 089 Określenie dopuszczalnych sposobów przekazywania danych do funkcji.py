# Lekcja 89 - Określenie dopuszczalnych sposobów przekazywania danych do funkcji.py

#-------------------------------------------------------------------------------------------------------


# Slash - "/" jeśli umieścimy ten znak w funkcji, na końcu, to oznacza, że można używać tylko argumentów
# NIE-nazwanych (pozycyjne)


def functionWithSlash (parameter1, parameter2 = 10, /):
    print(parameter1, parameter2)

# działa:
functionWithSlash("Test", 5) 

"""
nie działa, bo nazwaliśmy argumenty:
functionWithSlash(dupa = "Test", 5) 
functionWithSlash(parameter1 = "Test", parameter2 = 5) 
"""

#-------------------------------------------------------------------------------------------------------

# Gwiazdka - Jeśli umieścimy znak "*" na początku funkcji oznacza to,
# że oba argumenty funkcji muszą być nazwane, czyli musimy im nadać wartość przy wywołaniu funckji.

def functionWithStar (*, parameter1, parameter2):
    print(parameter1, parameter2)


# działa, bo nazwałem argumenty i ich nazwy pokrywają się z nazwami w definicji funkcji
functionWithStar(parameter1 = "kutas", parameter2 = "pizda") 
functionWithStar(parameter2 = "kutas", parameter1 = "pizda") # można zmieniać kolejność!!!

# nie działa, bo nazwy argumentów muszą być takie same jak w definicji funkcji:
""" 
functionWithStar(pizda = "kutas", kutas = "pizda") 
"""




