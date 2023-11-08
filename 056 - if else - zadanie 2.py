# Lekcja 56 - if else - zadanie 2


"""
Wymagania:
1. Dodaj zmienna experience z wartością 3, kolejną languages z listą elementów: "python", "typescript",
"javascript", "java".
Ostatnią zmienną będzie contractType o wartości "employment" jaką chce kandydat.
2. Wykorzystaj instrukcję if z operatorem and do sprawdzenia czy doświadczenie kandydata to dwa lub więcej lat
oraz czy zna język python i java.
3. Jeśli powyższe warunki są spełnione zrób kolejny if i sprawdź czy typ kontraktu
jest "b2b" lub "employment", pamiętaj o użyciu operatora or.
Zaprezentuj w terminalu informację, że kandydat jest przyjęty, gdy warunki są spełnione.
4. W przypadku, gdy warunki if nie są spełnione pokaż w konsoli po else odpowiednią instrukcję.
"""

experience = 1
languages =["python", "typescript", "javascript", "java"]
contractType = "employment"


if experience >= 3 and "python" in languages and "java" in languages:
    print("Warunek doświadczenia i językowy spełnione")
    if contractType == "employment" or "b2b":
        print("Oba warunki są spełnione")
else:
    print("warunki nie są spełnione")        

    
    
