# Lekcja 8 - Typ String - łańcuch znaków

str = "Hello world!"
print(str)
print(type(str))    # <class 'str'>
print(len(str))     # 12 (Hello to 5 + spacja to 1 + world to 5 + wykrzyknik to 1 = 12)
print(str[0])       # indeksy liczone są od zera, czyli poda pierwszą literę "H"
print(str[2])       # indeksy liczone są od zera, czyli poda trzecią literę "l"


print(str[ len(str) - 1 ], "ostatnia litera") # wyświetli ostanią literę (czyli indeks 11, bo liczone od zera)

subString0 = str[0:0] 
subString1 = str[0:1] 
subString2 = str[0:2] 
subString3 = str[0:3] 
subString4 = str[0:4] 
subString5 = str[0:5] 
subString6 = str[0:6] 
subString7 = str[0:7] 
print("---------------------------------------")

print(str[0], "test 0")
print(subString0, "test 1") # nie wyświetla nic! a powinno na logikę wyświetlać od 0, do 0 indeksu czyli 1-szą literę
print(subString0, "test 2") # kopia do testu
print(subString0, "test 3") # kopia do testu 

print(subString1) # tu dopiero wyświetla 1-szą literę, jak wyżej: subString1 = str[0:1] 
print(subString2)
print(subString3)
print(subString4)
print(subString5)
print(subString6)
print(subString7)


print("----------------------------------------")

print(str[4:]) #wyświetla od 4 indeksu do końca
print(str[::4]) #wyświetla co 2 indeks, od pierwszego

userName = input("podaj swoje imię  ")  #przyjmowanie z klawiatury
print("twoje imie to: ", userName)     

print("""ale jaja
panie ferdku działa te 
pisanie w kilku 
liniach""")

print('ale jaja\npanie ferdku działa te\npisanie w kilku\nliniach')

 