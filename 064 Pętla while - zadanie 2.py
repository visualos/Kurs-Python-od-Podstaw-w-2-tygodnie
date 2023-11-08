# Zadanie: Wyświetlanie elementów listy od końca z pętlą while

"""
Wymagania:
    1)  Stwórz listę elementów: Ania, Asia, Kasia, Basia
    2)  Zapisz zmienną i, od której w każdej iteracji pętli odejmiesz 1; to indeks
        elementu w liście. Wpisz wartość początkową zmiennej i jako ostatni indeks listy,
        czyli element "Basia"
    3)  W pętli while sprawdź, czy i jest większe lub równe zero.
        Pobierz imię z listy, używając numeru indeksu w i, i wyświetl je w konsoli.
        Zmień wartość zmiennej i.
"""


list = ["Ania", "Asia", "Kasia", "Basia"]
i=1

while i <= 4:
    print(list[len(list)-i]) 
    i += 1

