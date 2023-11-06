# Lekcja 17 - Typ Tuple - zadanie 1

# Stwórz krotkę tupleValues z wartośćiami :...
# Pokaż tryb krotki w konsoli
# Pokaż w konsoli ilość elementów krotki
# Pokaż ostatni element krotki
# Pokaż elementy od drugiego do szóstego
# Pokaż trzeci element od końca z ujemnym indeksem

tupleValues = 20, 40, 60, 80, 100, 120, 140
print(type(tupleValues)) 
print(len(tupleValues))
print(tupleValues[len(tupleValues)-1])
print(tupleValues[1:6])  #(40, 60, 80, 100, 120)
print(tupleValues[-3])