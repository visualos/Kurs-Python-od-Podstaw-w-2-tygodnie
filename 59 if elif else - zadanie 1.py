# 59 if elif else - zadanie 1

"""
Wymagania:
1.  Dodaj zmienną income z wartością 4000, która reprezentuje miesięczne dochody klienta.
2.  Dodaj zmienną creditScore z wartością 750, która reprezentuje ocenę kredytową klienta.
3.  Napisz instrukcje if-elif-else, które sprawdzą zdolność kredytową klienta na podstawie 
    jego dochodów i oceny kredytowej.
    a) Jeśli income >= 5000 i creditScore >= 800, klient otrzyma "Premium Offer"
    b) Jeśli income >= 3000 i creditScore >= 700, klient otrzyma "Standard Offer"
    c) W przeciwnym wypadku klient otrzyma "No Offer"
4. Wyświelt wynik w konsoli.

Uwaga: pamiętaj aby skorzystać z and aby jednym razem sprawdzić dwa warunki w instrukcji if np:
if v >= 1000 and clientAge >= 18:
    print("Oba warunki spełnione")

"""

income = 4000
creditScore = 750
clientAge = 20

if income >= 5000 and creditScore >= 800 and clientAge >= 18:
    print("Klient otrzyma Premium Offer")
elif income >= 3000 and creditScore >= 700:
    print("Klient otrzyma Standard Offer")
else:
    print("Klient nie otrzyma oferty")