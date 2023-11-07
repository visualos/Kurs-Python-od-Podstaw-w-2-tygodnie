# Lekcja 81 - Parametry czy argumenty w funkcji

"""
Informacje "parametry" i "argumenty" są często stosowane zamiennie w kontekście przekazywania
danych do funkcji, ponieważ programiści zwykle mają na myśli to samo. Jeśli jednak chcemy być
precyzyjni, warto pamiętać, że choć oba te terniny odnoszą się do tego samego zagadnienia, ich
znaczenie może się różnić w zależności od kontekstu:

Parametr to zmienna umieszczona w nawiasach okrągłych w definicji funkcji. Na przykład, w definicji
funkcji o nazwie sum znajdują się parametry a oraz b.
"""

def sum(a, b):  #to są parametry!!!
    return a + b 

# Argument to wartość przekazywana do funkcji podczas jej wywołania. Przykładowo, w poniższym 
# przypadku wartości 10 i 5 są argumentami przesyłanymi do funkcji:

sum(10, 5)  # to są argumenty!!!