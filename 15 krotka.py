# Lekcja 15 - Typ Tuple - krotka

# Krotka to uporządkowany ciąg danych, niemodyfikowalny zbiór utworzony za pomocą nawiasów okrągłych
# i elementów oddzielonych przecinkami. Krotkę można łatwo wyobrazić sobie jako pojedynczy rekord w 
# bazie danych dotyczący użytkownika, obejmujący informacje takie jak login, email, czy datę rejestracji.

# Krotki są niemutowalne. Operacje na krotkach generują nową wartość w pamięci :(.  


numberNames = ("jeden", "dwa", "trzy")

# Krotka zawierająca tylko jedną wartość musi zawierać przecinek po tym elemencie, co wskazuje na to,
# że chcemy utowrzyć krotkę, a nie łańcuch znaków:

fighters = ("f15",)
print(type(fighters), "Typ fightersów")           # <class "tuple"> 

emptyTuple = ()                 # pusta krotka musi mieć nawiasy

words = ("jeden", "dwa", "trzy", "cztery", "pięć", "sześć")
print("Typ wordsów", type(words)) # <class 'tuple'>


print(words[1])
print(words[1:4])
print(words[-1])
print(words[-3])
print(words[2:])
print(words[::2])
print(words[0:3]) # powtórka komend z lekcji 8 "Typ String - łańców znaków"


# Krotka wielopoziomowa/wielowymiarowa (zagnieżdżona)

nestedTuple = ((1, 2, 3), words)    # krotka wielowymiarowa, dwie krotki w jednej
print(nestedTuple[0][0])            # 1
print(nestedTuple[0][1])            # 2
print(nestedTuple[0][2])            # 3

print(nestedTuple[1][0])            # jeden


# Krotka jest niemutowalna, czyli nie można zmeniać jej elementów. Przy zmiania wyskoczy błąd.
# Można łączyć krotki dzięki konkatenacji:

tuplel = (10, 20, 30)
mergedTuples = tuplel + (40, 50, 60) # łączenie krotek (konkatenacja)
print(mergedTuples) # (10, 20, 30, 40, 50, 60)


# --------------------------------------------------------------------------------------------------------
# Operator in pozwala na sprawdzenie, czy wartość jest w krotce, tak jak w lekcji np. 12, 13
print(20 in (10, 20, 30)) # True

for value in (100, 200, 300):   # Iteracja po wartościach za pomocą pętli "for, in"
    print(value)                # 100
                                # 200
                                # 300

# --------------------------------------------------------------------------------------------------------
# Krotkę można usunąć, dzięki słówku del. Nie mylić z usuwaniem elementu krotki.
numTuple = (11, 22, 33 ,44)
print(numTuple)

del numTuple # usuwanie krotki


# --------------------------------------------------------------------------------------------------------
numbers = (12, 20, 36, 50) 
print(len(numbers))             # długość krotki, tak samo jak w listach
print("------------------------------\n")

# --------------------------------------------------------------------------------------------------------
names0 = "ania"                 # tworzy str ania
print(names0)
print("names0", type(names0))
print("\n")

names1 = ["ania", "tomek"]      # tworzy listę ['ania', 'tomek']
print(names1)
print("names1", type(names1))
print("\n")

names2 = "ania", "tomek"        # tworzy krotkę  ('ania', 'tomek')
print(names2)
print("names2", type(names2))
print("\n")

names3 = tuple(("ania", "tomek"))# tworzy krotkę ('ania', 'tomek')
print(names3)
print("names3", type(names3))
print("\n")

names4 = "ania" + "tomek"        # tworzy str aniatomek
print(names4)
print("names4", type(names4))
print("\n")


names5 = ("ania", "tomek")       # towrzy krotkę ('ania', 'tomek')
print(names5)
print("names5", type(names5))
print("\n")
 
names6 = ("ania" + "tomek")      # towrzy str aniatomek
print(names6)
print("names6", type(names6))
print("\n")

names7 = tuple("ania" + "tomek")  # towrzy tuple ('a', 'n', 'i', 'a', 't', 'o', 'm', 'e', 'k')
print(names7)
print("names7", type(names7))
print("\n")

names8 = tuple("ania")            # tworzy tuple ('a', 'n', 'i', 'a')
print(names8)
print("names8", type(names8))
print("\n")