# Lekcja 104 - Przydatne funkcje do operacji na krotkach

# Pamiętaj, że praca z krotkami, jakakolwiek, tworzy nową krotkę. Krotki są przecież niemutowalne.!!!

# Konkatenacja, czyli dodawanie 
krotka = (1, 2) + (3, 4) + (5, 6)
print(krotka)

# Mnożenie krotek
print(krotka * 3) # wypisuje krotkę trzy razy

# Logika w krotkach
print(4 in krotka)
print(10 not in krotka)

# Wypisywanie zawartości w krotkach
print(krotka[4])
krotka1 = krotka*3
print(krotka1[0:9])
print(krotka1[1:7])
print(krotka1[1:9:2])
print(krotka1[2:])
print(krotka1[:12])

# Wartość minimalna 'min(tuple1)'
print(min(krotka1))

# Wartość maksymalna krotki 'max(tuple1)'
print(max(krotka1))

# Lista na krotkę tuple([list])
list1 = [1, 2, 3, 4, 5]
print(tuple(list1), 'lista na krotke')