# Lekcja 78 - Tworzenie funkcji w Python - zadanie

# Zadanie z funkcjami
# 1. Stwórz krotkę z wartościami od -2 do 5
# 2. Napisz funkcję sumData(tuple) która zsumuje zawartość krotki i zwróć za pomocą return tą sumę
# 3. Wywołaj funkcję na krotce i pokaż wynik sumy w konsoli


krotka = (-2, -1, 0, 1, 2, 3, 4, 5)

print(krotka[1])

def sumData(tuple):
    sum = 0
    for num in tuple: # ciekawe: automatycznie num oznacza jako miejsce (adres), w krotce i się do
                        # niego odwołuje
        sum += num
    return sum

print(sumData(krotka))

