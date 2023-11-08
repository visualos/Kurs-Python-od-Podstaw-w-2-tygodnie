# Lekcja 63 - Petla while - zadanie 1

"""
Napisz program, który skorzyst z pętli while, aby dodać wartości od 1 do 120
1)  Dodaj zmienną "i" równą 0, która będzie powiększana w pętli o 1.
    Kolejną zmienną będzie sum z wartością początkową 0
2)  W pętli while sprawdź czy "i" jest mniejsze równe 120
    Wewnątrz pętli dodaj do sum wartość 1, następnie
    zrób inkrementację "i" o jeden.
3) Dodaj else po pętli while z tekstem w konsoli "Koniec pętli while"
4) Zapisz podsumowanie "Suma wartości: " oraz wynik sumy.

"""

i = 0
sum = 0

while i <= 120:
    sum += 1
    i += 1
else:
    print("Koniec pętli while")

print("Podsumowanie. Suma wartości i: " + str(i) + " Suma wartości sum: " + str(sum))