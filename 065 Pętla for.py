# Lekcja 65 - Pętla for

"""
Pętla for jest przeznaczona do iteracji po sekwencjach, takich jak listy, krotki, słowniki, zbiory czy ciągi znaków.
"""
# iteracja listy
listData = [1,"andrzej",3,4] 
print(type(listData))

for v in listData:
    print(v)

# iteracja krotki
tupleData = ("one", 2, "three")
print(type(tupleData))

for v in tupleData:
    print(v)

# iteracja zbioru
setData = {3,2,1, "pizda zimna"}
print(type(setData))

for v in setData:
    print(v)

# iteracja Stringa
strData = "Hello"
print(type(strData))

for v in strData:
    print(v)

# iteracja słownika
dictionaryData = {"Ola" : "ola@example.com", "Ania" :  "ania@example.com" }
print(type(dictionaryData))

for v in dictionaryData:
    print(v) # wyświetlanie jedynie KLUCZY słownika!!!
    print(dictionaryData[v]) # wyświetlanie jedynie WARTOŚCI słownika!!!

    # iteracja słownika
    for key, value in dictionaryData.items():
        print(key, " : ", value )
    else:
        print("KOOOONIEC")    
  
