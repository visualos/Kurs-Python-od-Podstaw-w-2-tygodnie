# 20 Typ Dict - słownik - ćwiczenie

bestComputerByYear = {
    2001: "Sony",
    2002: "IBM",
    2003: "Compaq",
    2004: "Sun",
    2005: "Sony",
    2006: "Lenovo",
}

bestComputerByYear[2007] = "Microsoft"

print("JESTEŚMY TUTAJ 1----------------", bestComputerByYear) #{2001: 'Sony', 2002: 'IBM', 2003: 'Compaq', 2004: 'Sun', 2005: 'Sony', 2006: 'Lenovo', 2007: 'Microsoft'}
print("JESTEŚMY TUTAJ 2----------------", "To jest typ zmiennej 'bestComputerByYear'", type(bestComputerByYear)) # <class 'dict'>
print("JESTEŚMY TUTAJ 3----------------", len(bestComputerByYear))

print("JESTEŚMY TUTAJ 4----------------", bestComputerByYear.keys ())
print("JESTEŚMY TUTAJ 5----------------", bestComputerByYear.values ())


for value in bestComputerByYear.keys():
    print("JESTEŚMY TUTAJ 6----------------", "Key:", value, "Values:", bestComputerByYear[value])

for key, value in bestComputerByYear.items():
    print("JESTEŚMY TUTAJ 7----------------", "Key:", key, "Values:", bestComputerByYear[key])

print("JESTEŚMY TUTAJ 8----------------", "0000000")

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------


# Zabawa w pobieranie kilku kluczy dla tego samego value (czyli na odwrót): Wzięte z forum
# https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/

# creating a new dictionary
my_dict ={"Java":101, "Python":100, "C Sharp":11, "Kotlin": 100}
print("JESTEŚMY TUTAJ 8.2----------------", my_dict)

# one-liner
print("JESTEŚMY TUTAJ 9----------------", "One line Code Key value: ", list(my_dict.keys())[list(my_dict.values()).index(100)])

# ---- moja autorska pętla szukająca kluczy dla jednej wartości
print("JESTEŚMY TUTAJ 10----------------", )
for value in my_dict.values():
    print("One line Code Key value: ", list(my_dict.keys())[list(my_dict.values()).index(value)])

    
dic ={"geeks": "B","for":"B","geeks":"C"}
 
value = {i for i in dic if dic[i]=="B"}
print("key by value:",value)


# function to return key for any value
 
def get_key(val):
   
    for key, value in my_dict.items():
        if val == value:
            return key
 
    return "key doesn't exist"
 
 
# Driver Code
my_dict = {"Java": 100, "Python": 100, "C": 11}
 
print(get_key(100))
print(get_key(100))


# input list (dictionary)
my_dict = {"Java": 100, "Python": 100, "C": 11}
value = 112
 
key_list = [key for key, val in my_dict.items() if val == value]
 
if len(key_list) > 0:
    print("The key for the value", value, "is", key_list[0])
else:
    print("Value not found in dictionary")

import re
 
# Given input
my_dict = {"Java": 100, "Python": 100, "C": 11}
value = 100
 
# Program code
pattern = re.compile(r'\b' + str(value) + r'\b')
key = next((k for k, v in my_dict.items() if pattern.search(str(v))), None)
print(key)

