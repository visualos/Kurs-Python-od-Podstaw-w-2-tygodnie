# Lekcja 75 - Przykładowy program w Python
# ostatnia lekcja w sekcji 4


"""
Kalkulator, który działa w terminalu
"""

currentNumber = 0
operation = None
resetCalculator = True
calcResult = None
calcOperationList = ["+", "-", "*", "/", "**"]

while True:
    if resetCalculator: 
        currentNumber = int(input("Podaj początkową liczbę: "))
        resetCalculator = False

    operation = input("Podaj operację arytmetyczną " + str(calcOperationList)
                      + " lub wpisz exit jeśli koniec lub reset: ")
    if operation == "exit":
        break
    if operation == "reset":
        resetCalculator = True
        continue


    allowedOperation = operation in calcOperationList
    if not allowedOperation: 
        print("Podana została nieobśługiwana operacja. Wybierz jedną z listy" + str(calcOperationList))
        continue

    secondNumber = int(input("Podaj drugą liczbę dla operacji: " + str(operation) + ": "))

    if operation == "+":
        calcResult = currentNumber + secondNumber
    if operation == "-":
        calcResult = currentNumber - secondNumber
    if operation == "*":
        calcResult = currentNumber * secondNumber
    if operation == "**":
        calcResult = currentNumber ** secondNumber
    if operation == "/":
        calcResult = currentNumber / secondNumber

    print("Wynik: " + str(currentNumber) + " " + str(operation) + " " + str(secondNumber) + " = " + str(calcResult))


    currentNumber = calcResult
    calcResult = None

    