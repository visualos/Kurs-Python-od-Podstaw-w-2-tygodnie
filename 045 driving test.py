# Lekcja 45 - Operatory logiczne - zadanie 2

"""
Zadanie - czy osoba może uczestniczyć w jakimś wydarzeniu mając 18 lat
lub bedąc pod opieką rodzica 
1) Użyj operatorów porównania oraz logiczego or, aby sprawdzić czy osoba może uczestniczyć w wydarzeniu.
2) Stwórz zmienne participantAge z wartością 15 oraz isWithParents jako True
3) Sprawdź w instrukcji if następujące warunki:
    - osoba musi mieć więcej lub równe 18 lat
    - osoba może uczestniczyć w wydarzeniu jeśli jest w towarzystwie rodziców
    Jeśli którykolwiek warunek jest spełniony, napisz w konsoli, że może uczestniczyć
    w wydarzeniu dla rodzin.
"""

participantAge = 15
isWithParents = True
if participantAge >= 18 or isWithParents == True:
    print("Może uczestniczyć w wydarzeniu dla rodzin")