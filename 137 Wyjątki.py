# Lekcja 137 - Wyjątki.py

"""
Obsługa wyjątków - programy w Python mogą reagować na różne nieprzewidziane błędy, dzięki czemu mimo problemów
mogą zareagować i kontynuować pracę.

poniżej wyjątek przerywa działanie programu:
"""
"""

data = ['Ania', 'Ola', 'Kasia']
print(data[2])
print(data[5]) # wyjątek, bo nie ma 5 indeksu w liście
"""
"""
Poniżej wyjątek jest obsłużony prawiłowo
"""

import sys # trzeba zaimportować sys do oblugi błędów:

data = ['Ania', 'Ola', 'Kasia']
print(data[2])

try:
    print(data[5]) # wyjątek, bo nie ma 5 indeksu w liście
except:
    print("Error: ", sys.exc_info()[0] )

print(data[0])