# Lekcja - 138 Wyjątki - ćwiczenie.py

# powtórka poprzednich lekcji
import sys

data = ['tosia','zosia', 'kupskosia']
print(data[0])



try:
    print(data[0])
    print(data[1])
    print(data[2])
    #raise Exception("some error!") #ręcznie wywołuje wyjątek typu Exception
    raise InterruptedError("some error!") #ręcznie wywłouje błąd


except IndexError: # można zostawic same exept. Wtedy złapie wszystkie błędy
    print('Error się pojawił', sys.exc_info()[0]) # zero zwraca typ błędu
except InterruptedError:
    print('InterruptedError się pojawił', sys.exc_info()[0])
except:
    print('Złapano wyjątek, Error się pojawił inny niż IndexError i InterruptedError')
else:
    print('koniec programu1')

print('Nie ma errorów')
"""
    
Funkcja sys.exc_info() zwraca trzy elementy:

Element o indeksie 0 zwraca typ wyjątku (np. IndexError, TypeError, itp.).
Element o indeksie 1 zwraca wartość, która jest instancją zgłoszonego wyjątku.
Element o indeksie 2 zwraca obiekt reprezentujący ślad stosu (traceback) wyjątku.
Jeśli użyjesz sys.exc_info()[2], otrzymasz dostęp do śladu stosu wyjątku, który zawiera informacje o miejscu, 
gdzie wyjątek został zgłoszony w kodzie.

Zmiana liczby w sys.exc_info()[n], gdzie n to liczba od 0 do 2, umożliwia dostęp do odpowiedniego elementu zwracanego przez 
funkcję sys.exc_info().

Jednakże, w praktyce, w większości przypadków najczęściej używa się sys.exc_info()[0], 
aby uzyskać typ zgłaszanego wyjątku, lub sys.exc_info()[1], aby uzyskać wartość instancji zgłaszanego wyjątku. 
Użycie sys.exc_info()[2] jest mniej powszechne, ponieważ głównie służy do uzyskania informacji o śladzie stosu dla debugowania.
    """