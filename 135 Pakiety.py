# Lekcja 135 - Pakiety

# Pakiety to po prostu pakiety modułów. Python udostępnia wiele pakietów stworzonych przez społeczność, które można
# zainstalować dzięki funkcji pip.
"""
W Pythonie, pakiet to sposób organizacji modułów, czyli plików zawierających kod Pythona. Pakiet składa się z katalogu, który zawiera pliki modułów oraz plik specjalny o nazwie __init__.py.

Oto główne cechy pakietów w Pythonie:

1.
Struktura katalogowa: Pakiety w Pythonie są reprezentowane przez katalogi, w których znajdują się pliki modułów. 
Wewnątrz katalogu reprezentującego pakiet, mogą znajdować się inne podkatalogi i pliki modułów.

Na przykład, jeśli mamy pakiet o nazwie moj_pakiet, jego struktura katalogowa mogłaby wyglądać tak:
moj_pakiet/
├── __init__.py
├── modul1.py
└── subpakiet/
    ├── __init__.py
    └── modul2.py

2.
Plik __init__.py: Plik ten jest wymagany w każdym katalogu reprezentującym pakiet. Może on być pusty,
ale może też zawierać kod inicjalizacyjny wykonywany podczas importowania pakietu.
 W starszych wersjach Pythona plik __init__.py był obowiązkowy, ale od wersji 3.3 Pythona, pakiet można utworzyć bez niego.
 """
# Plik __init__.py po prostu zbiera wszystkie moduły w pakiecie, tak żeby zaimportować tylko go. A on zaimportuje resztę
"""


3.
Importowanie modułów z pakietu: Aby importować moduły z pakietu, używa się notacji kropkowanej.
Na przykład, jeśli mamy pakiet moj_pakiet i moduł modul1 wewnątrz tego pakietu, można go zaimportować w ten sposób:
"""
from moj_pakiet import modul1
"""

4
Główny pakiet: Gdy nazwa pakietu jest używana jako część importowanego modułu, traktowana jest jako główny pakiet.
Na przykład, jeśli mamy pakiet moj_pakiet i moduł modul1 wewnątrz niego, importując moduł z poziomu zewnętrznego, można użyć:
"""
import moj_pakiet.modul1

"""
5
Pakiety pozwalają na lepszą organizację dużych projektów Pythona, grupując powiązane ze sobą moduły w odpowiednie struktury katalogowe. Umożliwiają też unikanie konfliktów nazw, ponieważ nazwy modułów są zagnieżdżone w ich pakietach.

Pakiety są kluczowym elementem organizacji kodu w Pythonie, pozwalając na lepszą strukturę projektów, 
podział kodu na logiczne jednostki oraz poprawę czytelności i zarządzalności kodu.

"""