# Lekcja 83 - Mutowalne i niemutowalne argumenty przekazywane do funkcji

# Przekazywanie wartości do funkcji w postaci parametrów - mutable vs immutable
# Podczas podczas definiowania funkcji oraz określania jej paeametrw, warto mieć
# na uwadze specyfikę typów dabych w Pythonie. Typy niemutowalne, takie jak int, float, tuple,
# str i bool, tworzą nowy obiekt wpamięci przy każdeh zmianie wartości. Z kolei typy mutowalne,
# takie jak set, list i dict, nie tworzą nowych obiektów w pamięci pofczas modyfikacji - ich 
# zawartość jest bezpośrednio zmieniana.

f = 3.2 # niemutowalne (int)
addr1 = id(f)
f = f + 2.5
addr2 = id(f)

print("pierwszy kutachong dla niemutowalnego intigera", addr1, addr2)
print("-----------------------------------------------------")

listData = ["a", "b"] # mutowalne (list)
addr1 = id(listData)

listData += ["c", "d"]
addr2 = id(listData)
print("drugi kutachong dla mutowalnej listy", addr1, addr2)

print("-----------------------------------------------------")
# przykład, że stringi są niemutowalne:
print("przykład, że stringi są niemutowalne")


def addToStr (string):
    string += "!"
    print("Nowa wartość po zastosowaniu funkcji to:", string)

string = "Hello"
print(id(string), " ID STAREGO STRINGA")
addToStr(string)
addToStr(string)
addToStr(string)
print(id(string), " ID SRODDKOWEGO STRINGA")
print("-----------------------------------------------------")
print("oryginalny: " + string)

print("-----------------------------------------------------")

string += "!!!!"

print(id(string), " ID NOWEGO STRINGA")
print("oryginalny: " + string) # nie dodały się wykrzykniki z funkcji, bo string nie można zmienić

print("-----------------------------------------------------")

# w "liście by się dodało", bo jest mutowalna

def addToList (someList):
    print("someList przed zmianą: " + str(someList))
    someList = [30, 40, 50]
    print ("someList po zmianie: " + str(someList))

listData = [2]
print(listData)

addToList(listData)
print(listData)
