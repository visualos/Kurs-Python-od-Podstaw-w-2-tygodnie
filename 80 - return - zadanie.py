# Lekcja 80 - return - zadanie.py

"""
Napisz program do konwersji funkcji czasu
1) Stwórz funkcję timeToSeconds przyjmującą ilość godzin oraz minut
    i zwracającą ilość sekund. Jako parametry funkcji zapisz: hours, minutes.
    Skonwertuj 2 godziny i 40 minut na sekundy i wynik pokaż w konsoli.

2) Stwórz funkcję timeToHours przyjmującą parametr minutes i zwracającą ilość godzin.
Skonwertuj 150 minut na godziny i wynik pokaż w konsoli.
"""

def timeToSeconds(hours, minutes):
    seconds = hours*3600 + minutes*60
    return seconds
print(timeToSeconds(2, 40))

def timeToHours(minutes):
    hours = minutes/60
    return hours
print(timeToHours(150))