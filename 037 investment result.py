# Lekcja 37 - Operatory matematyczne zadanie

"""
1. Oblicz zwrot z inwestycji po pół roku, zapisz poniższe zmienne:
    - initialInvestment - 8000
    - interestRate - 0.1 czyli 10%
    - inflation - 0.16 czyli 16%

2. Oblicz zwrot z inwestycji oraz o ile spadła wartość kapitału z uwagi na inflancję, 
    pokaż te kwoty w konsoli

3. Dodaj do kapitału zwrot z inwestycji oraz odejmij utracony kapitał z uwagi na inflancję, 
    pokaż wartość końcową w konsoli.
"""

#1

initialInvestment = 8000
interestRate = 0.1 
inflation = 0.16 

#2

initialReturn = initialInvestment * interestRate
print("Zwrot z inwestycji:", initialReturn)

lostValue = initialInvestment*inflation
(print("Utracona wartość: ", lostValue))

finalInvestment = initialInvestment + initialReturn - lostValue
print("Finalna kwota na koncie", finalInvestment)

