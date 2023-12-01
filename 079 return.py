# Lekcja 79 - return.py

# Definiowanie funkcji - return
# Return na końcu funkcji jest opcjonalne, umożliwia wyjście z funkcji w dowolnym momencie.

# Kończenie działania funkcji jeśli:
def printList(listData):
    if len(listData) <= 3:
        return

    print(listData)
    return #return na koncu jest opcjonalne jesli nie zwracana jest konkretna wartosc

printList(["a","b","c"])
printList(["a","b","c", "d", "e"])
