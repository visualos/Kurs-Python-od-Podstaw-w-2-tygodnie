# Lekcja 30 - Konwersja na bool
'''
Funkcja bool() przekształca wartość na wartość logiczną, czyli typ Boolean, który może
przyjmować jedną z dwóch wartości: True lub False, reprezentujących prawdę lub fałsz.

'''

# poniżej wartości, które daja False, tzw. Falsy values
print( bool()) # brak przekazanej wartości zwróci domyślnie False
print( bool(False)) # False
print( bool(0)) # False (równe dokładnie "0")
print( bool(0.0)) # False
print( bool( () )) # puste krotki dają False
print( bool( [] )) # puste listy dają False
print( bool( {} )) # puste zbiory dają False
print( bool("")) # pusty łańcuch znaków daje False
print( bool(None)) # None oznacza brak przypisanej wartości, również konwertuje na False


print( bool(True)) # True
print( bool(1)) # True
print( bool(5)) # True
print( bool(-10)) # True
print( bool( ("Ola", 1))) # krotka z przynajmniej jednym elementem True (False to różne od zera)
print( bool( [0] )) # listy z przynajmniej jednym elementem dają True
print( bool( {0} )) # zbiory z przynajmniej jednym elementem dają True
print( bool("x")) # String z przynajmniej jednym elementem daje True
