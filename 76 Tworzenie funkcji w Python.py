# Lekcja 76 - Tworzenie funkcji w Python.py

"""
Definiowanie funkcji
Funkcja to blok kodu, który może być wielokrotnie uruchomiony w celu wykonywania określonej czynności.
Funkcje są kluczowym elementem programowania w każdym języku, ponieważ oferują wiele gotowych
rozwiązań, np. jak print() do wyświetlania informacji w konsoli.
"""
"""
Definiowanie funkcji odbywa się za pomocą słowa kluczowego def, po którym umieszcza się nazwę
funkcji i nawiasy okrągłe. W nawiasach można podać parametry przekazywane do funkcji, oddzielone
przecinkami.
Nazwy zmiennych parametrów powinny być zgodne z konwencjami języka Python. Kod funkcji zaczyna
się od dwukropka i wymaga wcięcia. Funkcja może zwracać wartość, używając słowa kluczowego return.

Aby wywołać funkcję, należy wpisać jej nazwę, a następnie w nawiasach okrągłych prezkazać
listę parametrów.
"""
a = 3
b = 4

def addNumbers(num1, num2) : # parametry to lista zmiennych w definicji naszej funkcji
    result = num1 + num2
    return result

c = addNumbers(a, b) # argumenty to lista zmiennych wartości przekazanych do naszej funkcji
                        # prz wywołaniu
print(c)

d = addNumbers(c,10)
print(d)


def addNum(a, b):
    return a + b
def subNum(a, b):
    return a - b

value1 = addNum(56, 10)
value2 = subNum(56, 10)

print(value1)
print(value2)

print(subNum(54, 32) * addNum(subNum(5, 5), 10))


# Suma koszyka zakupów - przykładowy program
def calcBasketValue(basketList):
    basketSum = 0
    for key in basketList:
        print("Tutaj drukujemy key z pętli for: ", key)
        basketSum += basketList[key]
    return basketSum

shoppingBasket = {
    "smartphone" : 1200,
    "TV" : 1500,
    "console " : 1500
}


print("Tutaj drukujemy pierwszą wartość dla smartphone: ")
print(shoppingBasket["smartphone"])
print(calcBasketValue(shoppingBasket))