# Lekcja 34 - Mutowalność i niemutowalność - ćwiczenie

"""
immutable (zmiana tworzy nowy element w pamięci): int. float, bool, str, tuple, frozenset
mutable (zmiana wartości w tym samym miejscu pamięci): list, set, dict 
"""

# LICZBY CAŁKOWITE
a = 10
addr1 = id(a)

a += 1
addr2 = id(a)

print(addr1, addr2)
print(addr1 == addr2) # False

# FLOATY
a = 10.24
addr1 = id(a)

a += 1
addr2 = id(a)

print(addr1, addr2)
print(addr1 == addr2) # False

# LISTY
list = ["radek", "mariia", 0, 1, 20]
addr1 = id(list)
print("LISTY", list)


list += [5, 6, 7]
addr2 = id(list)
print(list)
print(addr1, addr2, addr1 == addr2) # True