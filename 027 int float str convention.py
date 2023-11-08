# Lekcja 27 - Konwersje typów - zadanie

'''
Wymagania:
1. Poproś użytkownika o wprowadzenie liczby całkowietej używając input(), pamiętaj że input() zwraca
    łańcuch znaków, więc musisz skonwertować tą wartość od użytkownika na faktyczną liczbę całkowitą
2. Poproś użytkownika o wprowadzenie liczby zmiennoprzecinkowej z input(), zrób konwersję str na float
3. Oblicz sumę liczby całkowitej i skonwertowanej na int liczby zmiennoprzecinkowej
4. Wyświetl wyniki obliczeń.
'''
#1
intNumber = int(input("Wprowadź liczbę całkowitą ")) # dodaje "int", bo domyślnie wpisuje liczbę jako str
print(intNumber)
print(type(intNumber)) 

#2
floatNumber = float(input("Podaj liczbę zmiennoprzecinkową, musi być z kropką "))

#3
suma = intNumber + int(floatNumber)  # domyślnie ustawiło suma na typ float, więc dałem int przy floatNumber
print(suma)
print(type(suma))
