# Lekcja 61 - Pętla while
"""
Pętla while kontynuuje wykonwyanie kolejnych iteracji, dopóki warunek jest spełniony, czyli zwraca warość True.
Kiedy warunek nie jest już spełniony, sterowanie programu przechodzi do instrukcji 
znajdującej się po pętli.
"""


number = 4
while number > 0:
    print(number)
    number = number -1 
print("kod po pętli")

# Pętla nieskończona
num = 5
while (True):
    print("Wprowadź w konsoli liczbę do pomnożenia, exit aby zakończyć")
    strData = input() # Odczyt danych od użytkownika
    if strData == "exit":
        break

    num *= int(strData)
    print("Nowa wartość po pomnożeniu " + str(strData) + " wynosi ", str(num))

print("Ostateczna wartość po pętli " + str(num))

number = 5
while number >= 0:
    print(number)
    number -= 1
else:
    print("Warunek nie jest już spełniony, bo number = " + str(number))
