# Lekcja 134 - Moduły oraz __name__ i reload

# funkcje w osobnym pliku
# mathModule.py

def addNumber(a, b):
    print("mathModule.__name__: " + __name__)
    return a + b

addNumber(5,6)

# moduły - reload
# Każdy import wykonuje kod z zaimportowanego pliku.

#plik otherTest
import random
print("random from otherTest.py" + random.randint(0, 100))

# plik otherProg.py
# import otherTest impoertuje i wykonuje kod w module
import otherTest
import importlib # tutaj mamy dostęp do metody reload

print('OtherProg test')
# reload importuje wcześniej zaimportowany moduł
importlib.reload(otherTest)
importlib.reload(otherTest)

# Z CHATAGPT" -----------------------
from importlib import reload
import mathModule

# Po pewnym czasie, jeśli zmieniłeś kod w mathModule, możesz użyć reload, aby ponownie wczytać moduł.
reload(mathModule)

#-------------------------