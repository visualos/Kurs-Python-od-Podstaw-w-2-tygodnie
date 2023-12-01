# Lekcja 103 - Przydatne funkcje do operacji na listach
# Praca z listami powtórka

list1 = [1, 2, 3, 4, 'Adamek', 'Sobota', 'pizdeczka']
print(list1,' cała lista')
print(list1[2])
print(list1[4])

print(list1[0:2])
print(list1[0:8:2])

del list1[2]
print(list1,' cała lista')

print(list1[2])
print(list1[4])

print(list1[0:2])
print(list1[0:8:2])
print('-----------------')
print(list1[:2])
print(max([1,2, 3, 5]))
print(min([1,2, 3, 5]))

krotka = (1, 2, 3, 4, 5)
lista = list(krotka)

print(lista)

# Łączenie list
list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 3, 4, 5, 6]
list4 = list1 + list2
print(list1 + list2)

# Logika w listach
print(2 in list1)
print(4 not in list2)

# Pętle na listach
for x in list1:
    print(x)

# Dodawanie w listach, czyli list4.append

list2.append('samuraj')
print(list2)

# Ilość powtórzeń 'list4.count()
print(list4) 
print(list4.count(6))

# Dodanie elementów do listy z innej sekwencji 'list4,extend()'

print(list4)
print(list4.append('Tomek'), list4)
print(list4.extend(['Kasia', 'Tomek']), list4)

# Dodawanie elementu na odpowiednie miejsce: list4.insert
print(list4)
list4.insert(2, 'Radek')
print(list4)

# Odwrócenie koljenści listy 'list4.reverse()
list4.reverse()
print(list4)

#przykład na samej pętli for od Chata GPT:
oryginalna_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odwrocona_lista = [oryginalna_lista[i] for i in range(len(oryginalna_lista) - 1, -1, -1)]
print(odwrocona_lista)

# Sortowanie listy 'lista.sort() 
oryginalna_lista.sort()
print(oryginalna_lista)

# Zwraca i zabiera ostatni element z listy 'lista.pop'
print(list4.pop())
print(list4)
