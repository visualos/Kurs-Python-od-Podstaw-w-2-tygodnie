# Lekcja 50. Operatory tożsamości is oraz is not

"""
Operatory tożsamości (identity operators) - is, is not

Porównują one miejsce w pamieci, na które wskazują operandy. W przypadku operatora "is",
jeśli oba operandy wskazują na to samo miejsce w pamięci, zwracana jest wartość true.
Natomiast w przypadku operatora "is not", zwraca wartość true, gdy operandy nie wskazują
na to samo miejsce w pamięci.

"""


a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]

print(a is b) # 'is' wskazuje na miejsce w pamięci
print(a is a)
print(b is a)
print(b is b)

# Lekcja 51 - ćwiczenie

listA = [1,2,3,4,5]
listB = [6,7,8,9]
listC = listA
print(listA is listC) # True

print(dir(listC))
listC.append(45)  # nie ma znaczenia czy odwołujesz się do listA, czy C. Licba 45 jest dodawana w obu listach!
print(listC) # dowód na zdanie powyżej
print(listA) # dowód na zdanie powyżej

print(listA is listC) # True
print(listA is not listB) # True