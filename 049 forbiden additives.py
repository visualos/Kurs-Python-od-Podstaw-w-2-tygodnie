# Lekcja 49 - Operatory przynależności - zadanie 2

"""
Zadanie - czy podany dodatek nie znajduje się na liście zakazanych dodatków do żywności.
1) Użyj operatora przynależności not in..(...)
"""

forbidenAdditives = ['rtęc', 'aluminium', 'kadm', 'ołów']
additiveToCheck = "żelazo"

if additiveToCheck not in forbidenAdditives:
    print("Dodatek nie jest na liście zakazanych substancji,")