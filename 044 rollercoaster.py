# Lekcja 44 - Operatory logiczne - ćwiczenie

"""
Zadanie - czy osoba może przejechać się rollercoasterem?

1) Użyj operatorów porównania i logicznego and aby
    sprawdzić czy osoba może przejechać się kolejką.
2) Stwórz zmienne personalAge z wartością 14 i personalHeight jako 160
    - osoba musi mieć więcej lub równa 12 lat
    - osoba musi mieć więcej lub równe 150 cm wzrostu
    Jeśli oba warunki są spełnione napisz w konsoli, 
    że może przejechać się rollercoasterem.
"""

personalAge = 10
personalHeight = 160

if personalAge >= 12 and personalHeight >= 150:
    print(" Możesz przejechać się kolejką.")
else:
    print(" Nie możesz.")