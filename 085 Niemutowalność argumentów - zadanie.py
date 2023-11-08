# Lekcja 85 Niemutowalność argumentów - zadanie.py

# Zadanie na przekazanie danych do funkcji przez wartość
"""
1) Napisz funkcję raiseWage z dwoma parametrami liczbowymi: income oraz extra
2) W funkcji podnieś wartość income o 20%. Następnie zwróć sumę income i extra.
3) Stwórz zmienną wage poza funkcją o wartości 5000
4) Wywołaj funkcję raiseWage przekazując jako argument wage oraz 1000 jako extra.
    Zachowaj zwracaną wartość w zmiennej updateWage
5) Pokaż w konsoli wartości: wage i updatedWage, ponieważ przekazywane dane są niemutowalne
    to wage musi mieć wartość 5k, a updatedWage odpowiednio większą według implementacji funkcji.

"""

def rasiseWage(income, extra):
    income *= 1.2
    return income + extra

wage = 5000
updateWage = rasiseWage(wage, 1000)

print(wage)
print(updateWage)
print(wage)
