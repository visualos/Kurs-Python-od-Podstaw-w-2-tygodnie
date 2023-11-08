# Lekcja 97 - Przydatne funkcje do operacji matematycznych

# zmiana typu danych:

string = str(12.56)
print(string)
print(type(string))

listData = str( [0, 1, 2, 3] )
print(listData)
print(type(listData))
print(len(listData))

number = int('67')
print(type(number))

number2 = float('20.03')
print(type(number2))


import math
# wartość bezwzględna
print(abs(-5))

#zaokrąglenie do największej liczby całkowitej nie większej niż podana wartość
print(math.floor(6.78))
#zaokrąglenie do najmniejszej liczby całkowitej nie mniej niż podana wartość
print(math.ceil(6.78))

#max zwróci największą liczbę z przekazanych
print(max(12, 3, 78, 32, 11))

#min zwróci najmniejszą wartość z przekazanych
print(min(12, 3, 78, 32, 11))

#pow (power) podnosi do potęgi
print(pow(3,3))

# sqrt - pierwiastek
print(math.sqrt(16))

# round - zaokrągla do podanej ilości miejsc po przecinku
print(round(23.12345, 3))


import random
#random
print(random.random()) # losowy float od 0 do 1

#random choice - losowy element z listy, krotki lub str
print(random.choice([1, 2, 3, 400]))

#randrange - losowy element z zakresu statr, stop, step
print(random.randrange(0,25,5))

# shuffle - ustawia losowo elementy listy
listData = [0, 1, 2, 3, 4]
print(random.shuffle(listData))
print(listData)

# uniform - losowy float większy of x i mniejszy od y
print(random.uniform(1,49))


#dodatkowo Python oferuje wiele funcji takich jak tangens cotangens itp.