# Lekcja 51 - Operatory tożsamości - ćwiczenie


listA = [1,2,3,4,5,6]
listB = [6,7,8,9]

listC = listA
print("Czy listC wskazuje na to samo miejsce w pamięci co listA:", listA is listC) # True

print(dir(listC))

listC.append(45)
print(listC)
print(listA)