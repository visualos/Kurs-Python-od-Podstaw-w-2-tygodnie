# Lekcja 105 - Praca ze słownikami.py


# Praca ze słownikami
data = {'name' : 'Kasia ', 'city' : 'Waw'}

# Pobranie elementu zkey name, Kasia 
print(data['name'])

# Modyfikacja elementu:
data['name'] = 'Radek'
print(data)

# Dodanie elementu do tablicy
data['nowy'] = 'nowy uczestnik'
print(data)

# Dodanie wartości dla istniejącego już klucza: dictonary['klucz'].append['kolejna_wartość_dla_klucza']
my_dict = {'klucz': ['wartość1', 'wartość2']}
my_dict['klucz'].append('wartość3')
print(my_dict['klucz'])  # Wypisze ['wartość1', 'wartość2', 'wartość3']



# Skasowanie elementu 'del' - można wpisać tylko klucz
del data['name']
print(data)

# Skasowanie wszystkich elementów - 'nazwa_słownika.clear(). Słownik dalej jest, ale pusty
data.clear()
print(data)

# Długość słownika - len(nazwa_słownika)
print(len(data))

# Kopia słownika nazwa_słownika.copy() - To jest płytka kopia!!!
data = {'name' : 'Kasia', 'miasto' : 'Waw'}
data1 = data.copy() # data1 (kopia) wskazuje na ten sam obiekt w pamięci co data
print(data1)

# Tworzy słoniki z podanymi kluczami, wartość none data.fromkeys()
print('słownik z podanymi kluczami', data.fromkeys(("name", 'miasto', 'cos tam jeszcze'),'moze byc puste, wtedy = none')) # jak dam jeden nawias mniej, to kluczem będą pojedyncze literki!!
print(data.fromkeys("name", 'aleoiuoiuoiuo')) # jak dam jeden nawias mniej, to dla literek ze słowa po lewej
                                              # przypisze wartość po lewej ('n' : 'aleoiuiuoiuo, ...)
print(data)
data['name'] = 'Genowefa'
print(data)

# Zwraca istniejącą wartość klucza lub drugi argument: 'data.get()'
print(data)
print(data.get('name'), "\n")

print(my_dict)
print(my_dict.get('klucz'),'\n')
        # lub drugi argument:

data['dodajemy_klucz'] = "i jego wartość"
print(data)
print(data.get('KLUCZ KTÓREGO NIE MA, JAK JEST TO WYŚWIETLI jego wartość',  'DEFAULT' ), 'tutaj', '\n')

# czy klucz jest w słowniku: "klucz" in data
print('Genowefa' in data)
print('name' in data, '\n')

# zwraca listę kluczy data.keys()
print(data.keys())

# zwraca listę wartości data.values()
print(data.values())

#






