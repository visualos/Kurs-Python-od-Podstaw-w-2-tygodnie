# Lekcja 88 - Domyślne argumenty funkcji i nazwane argumenty - zadanie.py

"""
Funkcja z domyślnymi wartościami parametrów
1) Napisz funkcję z parametrami:
    - email
    - country z domyślną wartością "USA"
    - company z domyślną wartością "Sample Corp"
2) Zwróć z funkcji słownik z elementami jak parametry
3) Przetestuj funkcję z jednym argumentem john@example.com
    oraz drugi przypadek z jane@example.com.
"""

def worker(email, country = "USA", company = "Sample Corp"):
    return {
        "email" : email,
        "country" : country,
        "company" : company
    }

print(worker("john@example.com -----------------------"))  

# To samo tylko, że z pętlą napisane przez chata GPT.
def worker(email, country="USA", company="Sample Corp"):
    result = {}
    for arg_name in ["email", "country", "company"]:
        result[arg_name] = locals()[arg_name]
    return result

print(worker("john@example.com"))