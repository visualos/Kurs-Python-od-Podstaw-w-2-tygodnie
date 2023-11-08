# Lekcja 86 - Mutowalne argumenty - zadanie


"""
Przekazywanie mutowalnych danych do funkcji jak słownik, zadanie:
1) Utwórz słownik opisujący pracownika i zapisz go w zmiennej worker. Do elementów słownika 
dodaj name, email, rank (stopień - wpisz programmer), salary (8000)
2) Napisz funkcje elevateToMenager, która przyjmuje parametr o nazwie person, gdzie przezkazany
będzie słownik.
3) Wewnątrz funkcji zmień wartości elementów przekazanego słownika person, podnieś pensję o 50%,
zmień rank na menager. Dadatkowo sprawdź czy przypadkiem przekazany pracownik już nie jest menagerem,
w takim wypadku podaj w konsoli, że osoba ta jest już menagerem i wyjdź z funkcji, pokaż w konsoli
czy został on zaktualizowany.

"""

worker1 = {
    "name" : "name",
    "email" : "email",
    "rank" : "programmer",
    "salary" : 8000
    }

worker2 = {
    "name" : "name",
    "email" : "email",
    "rank" : "menager",
    "salary" : 8000
    }

print(id(worker1))
print(id(worker2))
def elevateToMenager(person):
    if person["rank"] == "menager":
        print("Ta osoba jest już menagerem")
        return
    else:
        person["rank"] = "menager"
        person["salary"] *= 1.5


print(elevateToMenager(worker1))
print("Awans programmera------------------------------, ", worker1)
    
print(elevateToMenager(worker2))
print("Awans menagera------------------------------", worker2)

print(id(worker1)) # te same adresy co na początku, czyli ok
print(id(worker2))