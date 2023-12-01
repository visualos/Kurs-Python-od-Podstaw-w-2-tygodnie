# Lekcja 33 - Mutowalność i niemutowalność

"""
Mutowalność vs niemutowalność
W Pythonie typy danych można podzielić na dwie kategorie: mutowalne i niemutowalne.
Mutowalne typy pozwalają na zmianę wartości, podczas gdy niemutowalne tego nie umożliwiają.

W analizie wykorzystamy specjalną funkcję id(), która zwraca unikatowy identyfikator dla każdego
podanego obiektu. W praktyce jest to liczba całkowita wskazująca miejsce w pamięci, gdzie
przechowywana jest wartość. Należy pamiętać, że w Pythonie wszystko jest obiektem, w tym liczby
całkowite, liczby zmiennoprzecinkowe, krotki itp.

"""

a = 10
b = 20
print( id(a) ) # 140728895464520
print( id(b) ) # 140728895464840
print( id(a) == id(b) ) # False


"""
Zmodyfikowanie wartości zmiennej "a" w przykładzie poniżej, spowodowała utowrzenie nowej liczby całkowitej
w pamięci z nową wartością 2. Zmienna "a" wskazuje teraz na tę nową wartość. Oryginalny obiekt liczby
całkowitej nie mógł zostać zmieniony, ponieważ jest NIEMUTOWALNY, co doprowadziło do stworzenia nowego
obiektu w pamięci = więcej pamięci zostało użyte.
"""

a = 1
addr1 = id(a)

a += 1 #zwiększa zmienną "a" o jeden
addr2 = id(a)

print(addr1, addr2)
print(addr1 == addr2)   # False, czyli zwiększając liczbę całkowitą o jeden, tak
                        # naprawdę tworzymy nową liczbę, zajmujemy dodatkową pamięć.