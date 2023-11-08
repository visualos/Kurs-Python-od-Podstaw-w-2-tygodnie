# Lekcja 69 - Pętla for z range

"""
for - pętla z range 
Funkcja range generuje ciąg liczb, domyślnie rozpoczynający się od zera i zwiekszając się do wartości
podanej minus 1. Na przykład range(7) stworzy sekwencję [0,1,2,3,4,5,6]


"""

i = range(7)
print(i)
print("range(3) w pętli ")
for v in range(3):
    print(v)

print("range(7) w pętli ")    
for v in range(7):
    print(v)


# range(start, end, step)
print("range(2, 8, 2) w pętli ")
for v in range(2, 8, 2):
    print(v)