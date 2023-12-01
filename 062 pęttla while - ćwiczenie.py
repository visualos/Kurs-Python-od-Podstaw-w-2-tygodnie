# Lekcja 62 - pętla while - ćwiczenie

counter = 6 
while counter >= 0:
    print(counter)
    counter -= 1
    print("Koniec")


sum = 0
counter = 6
while counter >= 0:
    value = input("Podaj liczbę do dodania ")
    if value == "exit":
        break
    counter -= 1
    sum += int(value)
    print("Suma dodanych liczb wynosi "+ str(sum))
else:
    print("koniec petli")