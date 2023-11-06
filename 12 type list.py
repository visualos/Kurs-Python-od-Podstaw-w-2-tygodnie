# Lekcja 12 - Typ list
# Typ list, czyli lista w nawiasach kwadratowych


brands = ["Sony", "Ford", "Opel"] # tworzenie listy
print(type(brands)) # <class 'list'>

print(brands[0]) # wywołanie pierwszej pozycji z listy (Sony)
print(brands[len(brands) - 1 ]) # wyświetla ostatni element listy

print(brands[-1]) # też wyświetlna ostatni element z listy. Fajna sztuczka / skrót
print("brands[0:2]", brands[0:2]) # wyświetla od pierwszego indeksu, w sumie dwa.

brands[1] = "mercedes" # zamienia drugi indeks
print(brands)

brands.append("GMC") # dodaje na koniec listy
print(brands)

brands.insert(0, "Lenovo")  # dodaje Lenovo na pierwszy indeks, a reszte przesuwa
print(brands)               # ['Lenovo', 'Sony', 'mercedes', 'Opel', 'GMC']



print("Sony" in brands) # sprawdza czy Sony jest na liście (True/False)

if "Sony" in brands:                # też sprawdza
    print("Sony jest w brands")


del brands[1] # usuwa 2 indeks czyli "Sony"
print(brands)