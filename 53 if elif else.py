# Lekcja 53 - if elif else
'''
if - instrukcja warunkowa do podejmowania decyzji w programie

Podczas działania aplikacji może wystąpić wiele różnych okoliczności wymagających reakcji, takich jak interakcje
użytkownika, otrzymanie nowych danych z sieci itp. Zazwyczaj proces podejmowania decyzji opiera się na użyciu
instrukcji warunkowej if albo else.
'''
'''
Instrukcja if wywołuje wyrażenie i jeśli jego rezultat będzie True to wykona blok kodu. (uwaga na wcięcia).
'''

checkNumber = 12 

if checkNumber > 8:
    print("check number większe od 8")
    print("też się wyświetli jeśli checkNumber > 8")
    if checkNumber > 8:                             # instrukcja zagnieżdżona, która się wykona
        print("printNumber większ od 8")

if checkNumber == 5:
    print("checkNumber równe 5")
    if checkNumber > 8:                             # instrukcja zagnieżdżona, która się NIE wykona
        print("printNumber większ od 8")
elif checkNumber > 8:
    print("checkNumber jest większy od 8 PONOWNIE")
else:
    print("coś innego")


'''
Krótszy zapis
'''
a = 15                                              
b = 7
if a > b: print("a większe od b")                   # krószy zapis (aby zadziałało elif, else trzeba dać wcięcie!)
