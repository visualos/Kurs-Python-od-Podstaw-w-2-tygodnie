# Lekcja 112 - Konstruktor

# Kontruktor to automatyczny byt pojawiający się przy tworzeniu klasy. Rozumiem to tak, że musimy go stworzyć tak czy siak.
# Ale ziomek napisał, że może czyli nie musi. Na dole to co on napisał:

"""
W klasie może być zdefiniowana specjalna metoda tzw. konstruktor o nazwie __init__. Będzie wywołana podczas tworzenia instancji obiektu
np: person2 = Person('Ala', 'Test', 'UK'). Konstruktor zwykle stosuje się do zainicjonowania zmiennych wewnątrz klasy wartościami
z argumentów przekazanych do konstruktora oraz innymi potrzebnymi operacjami.
"""

# To ten piździułek co ma dwa podrkeślniki, nazwę i znowu dwa podkreślniki - __init__(self, zmienna1, zmienna2, ...):
#

"""
I teraz uwaga od ziomeczka: 
Każda metoda w klasie, w tym konstruktor zawsze przyjmuje obowiązkowy pierwszy argument self, który wskazuje na aktualny
obiekt na którym operujemy podczas wywołania metody/konstruktora. Dzięki self możemy zmzienić wartości zmiennych w obiekcie
oraz wywołać inne metody.
"""