# Lekcja 102 - Łańcuchy znaków - czyszczenie tekstu - zadanie 2

# Zadanie String replace
# 1) Stwórz funkcję cleanText, która będzie czyścić
# przekazany tekst z określonych słów. # 
# 2) Użyj funkcję replace do zamiany podanych słów na
# wykropkowane, które wielokrotnie może pojawić się w przekazanym łańcuchu. Dla uproszczenia będziesz 
# zamieniać nazwy języków programowania ;) np.
# php zmienisz na *** java na **** itd
#
# 3) Zastąp następujące słowa kluczowe:
# JavaScript, java, php, html, css
# 4) Zwróć wyczyszczony tekst z funkcji cleanText.
# 5) Wywołaj funkcję na następującym lub podobnym tekście:
#
"""Programowanie zacząłem z językiem php, następnie
# poznałem: html i css, ale obecnie skupiam się na
# JavaScript"""

# Wynik pokaż w konsoli.


def cleanText(tekst):
    tekst = tekst.replace('java', '****')
    tekst = tekst.replace('php', '***')
    tekst = tekst.replace('html', '****')
    tekst = tekst.replace('css', '***')
    print(tekst)

cleanText('Programowanie zacząłem z językiem php, następnie poznałem: html i css, ale obecnie skupiam się naJavaScript')