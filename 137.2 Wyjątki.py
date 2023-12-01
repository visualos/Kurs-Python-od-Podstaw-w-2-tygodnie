# Lekcja 137.2 - Wyjątki.py

# Obsługa wyjątków - dodatkowo można wskazać konkretny wyjątek, który ma być obsłużony np. IOError
# dla błędów podczas pracy z plikami

"""
Chat GPT musiał znowu pomóc z moim przepięknym tourorialem:

import os jest to polecenie importowania modułu o nazwie os w Pythonie. 
Moduł os jest częścią standardowej biblioteki Pythona i zapewnia interfejs do funkcji związanych z systemem operacyjnym, 
umożliwiając interakcję z funkcjonalnościami systemowymi.

"""
import os
# sometimes script runs in diffreent folder
# from where it is located

# nagle się chujek na angielski przerzucił. Skopiował to od kogoś a jak inaczej.

script_dir = os.path.dirname(__file__)
"""
Pobiera ścieżkę bezwzględną do uruchamianego skryptu. `os.path.dirname(__file__)` 
zwraca ścieżkę katalogu bieżącego skryptu.
"""

print(script_dir) # absolute path to runned script

fh = None

"""
IOError w Pythonie jest wyjątkiem zgłaszanym, gdy występują problemy z operacjami wejścia/wyjścia (I/O). 
W Twoim kodzie, blok try...except próbuje otworzyć plik o nazwie "test.txt" w trybie zapisu ("w"). 
Gdy plik zostaje otwarty, program próbuje zapisać treść "content" do tego pliku.
"""
try:
    fh = open(script_dir + "/test.txt", "w")
    fh.write('content')
except IOError:
    """
    W bloku except IOError:, jeśli wyjątek IOError zostanie zgłoszony (czyli coś poszło nie tak podczas operacji wejścia/wyjścia), 
    program wyświetli komunikat "IOError occured". Jest to sposób na obsługę sytuacji, w której operacje na plikach nie powiodły 
    się z jakiegoś powodu.
    """
    print('IOError occured')
else:
    print('closing file')
    fh.close() # "Zamyka otwarty plik."

"""
W programie otwarto plik w tej samej ścieżce co skrypt. Jest obsługa błędu jeśli zaistnieje.
Jeśli wszystko jest w porządku jak nie będzie błędu po else zostanie zamknięty dostęp do pliku.
"""

