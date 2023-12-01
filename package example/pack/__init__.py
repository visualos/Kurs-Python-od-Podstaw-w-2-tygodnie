# Lekcja 136 - Pakiety - ćwiczenie

# Od wersji Pythone 3.3 plik nie jest obowiązkowy, ale jest w kursie więc robimy to.

from pack import * # możemy zainicjować wszystko po kolei, albo napisać gwiazdkę tak jak tutaj. Ten sposób może powodować
#                   błędy

"""
Warto pamiętać, że używanie from pack import * jest generalnie odradzane ze względu na ryzyko konfliktów nazw i
utraty czytelności kodu. Zamiast tego, zaleca się importowanie tylko konkretnych symboli, 
które są potrzebne w danym module, co pozwala na jasne i precyzyjne zarządzanie importowanymi elementami.
"""
from pack.book import Book # to jest bardziej precyzyjne i zalecane

from pack.functions import addNums # to dodałem od siebie dla treniengu
