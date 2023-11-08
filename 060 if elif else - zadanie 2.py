# 60 if elif else - zadanie 2

"""
Wymagania:
1. Dodaj zmienną score z wartością 85, która reprezentuje wynik ucznia w procentach.
2. Napisz instrukcję if-elif-else, które przypisza ocenę uczniowi na podstawie jego wyniku:
    a) Jeśli score >= 90, uczniowi przypisuje 5/
    a) Jeśli score >= 80, uczniowi przypisuje 4/
    a) Jeśli score >= 70, uczniowi przypisuje 3/
    a) Jeśli score >= 60, uczniowi przypisuje 2/
    a) Jeśli score >= 50, uczniowi przypisuje 1/
3. Wyświetl wyniki w konsoli

"""

score = 30

if score >= 90:
    print("Dostajesz 5")
elif score >= 80:
    print("Dostajesz 4")
elif score >= 70:
    print("Dostajesz 3")
elif score >= 60:
    print("Dostajesz 2")
else:
    print("Dostajesz 1")
