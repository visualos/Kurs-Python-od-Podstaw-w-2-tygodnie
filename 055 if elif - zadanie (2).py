# Lekcja 55 - if elif - zadanie

"""
Wymagania:
1. Dodaj zmienną age o wartości 28 oraz weight = 75
2. Napisz instrukcję if-else sprawdzającą, czy kandytat ma wiek większy lub równy 18, jeśli tak, 
    sprawdź kolejną instrukcją if-else, czy jego waga jest większa równa 50.
    Jeśli oba warunki są spełnione, napisz w konsoli, że może oddać krew.
3. W przypadku gdy jakiś warunek nie jest spełniony, to po else napisz w konsoli dlaczego.
"""

age = 18
weight = 50

if age >= 18:
     if weight >= 50:
        print("Kandytat może oddać krew")
    else:
        print("za chudy!")
