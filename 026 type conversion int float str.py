# Lekcja 26 - Konwersje typów - ćwiczenie

floatNumber = 47.25346253
intNumber = int(floatNumber) # zmiana typu na int
print(type(intNumber))  # <class 'int'>
print(intNumber)        # 47


float2 = float(intNumber)
print(type(float2))     # <class 'float'>
print(float2)           # 47.0

int2 = int("   234234") # zmiana na int
print(int2)             # 234234
print(type(int2))       # <class 'int'>

print("Liczba to jest taka a taka " + str(int2)) 