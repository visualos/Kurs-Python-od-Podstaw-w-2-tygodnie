# Lekcja 48 - Operatory przynależnośći - zadanie

"""
Zadanie - czy podany kolor znajduje się na liście ulubionych kolorów
1) Użyj operatora przynależności in, aby
    sprawdzić czy dany kolor jest na liście ulubionych kolorów.
2) Stwórz listę favoriteColors z wartościami red, blue, green, yellow.
3) Stówrz zmienną colorToCheck z wartością blue
4) Sprawdź w instrukcji if, czy colorToCheck znajduje się na liście favoriteColors.
    Jeśli warunek jest spełniony, napisz w konsoli, 
    że kolor jest na liście ulubionych kolorów.

"""

favoriteColors = ['red','blue','green', 'yellow']
colorToCheck = 'blue'

if colorToCheck in favoriteColors:
    print("Kolor jest na liście ulubionych kolorów.")