# Lekcja 106 - Przydatne funkcje do operacji na datach

# Musimy zaimportować bibliotekę 'time'

import time

# na skróty
print('-----------------NA SKRÓTY--------------------------')

print('------"type(time.time())": - sprawdzenie typu zmiennej: ', type(time.time()))
print('------"type(time.localtime())": - sprawdzenie typu zmiennej: ', type(time.localtime()),'\n')

print('------time.time() = ilość sekund od 1.01.1970: ', time.time(), '\n' )
# Z ZEREM i ŻADNYM INNYM NIE DZIAŁA!!!:
#print(' time.time(0) = ilość sekund od 1.01.1970: ', time.time(0), '\n' )

print('------time.localtime() - wyświetla aktualny czas: ', time.localtime(), '\n')
print('------time.localtime(0) - wyświetla czas "WIELKIEGO POCZĄTKU, CZYLI 1.01.1970: ', time.localtime(0), '\n')
print('------time.localtime(1) - wyświetla czas "WIELKIEGO POCZĄTKU + 1 SEKUNDA, CZYLI 1.01.1970 + JEDNA SEKUNDA: ', time.localtime(1), '\n')

print('-----------------SPRAWDZENIE PROSTEJ LOGIKI FUNKCJI--------------------------')
print((  (time.localtime(time.time()))   ==   (time.localtime())   ), ' równa sie')
print(time.localtime(time.time()))


# Czas który minął przez ostatnie 7000 dni:
licznik = time.localtime(time.time()-7000*24*60*60)
print(licznik)

# NOWY SLAJD NOWE MOŻLWOŚCI
# Formatowanie w wygodny sposób daty podanej przez time.localtime(): time.asctime()
print('-----------------NOWY SLAJD 2---------------------------------------------------')
print('------time.asctime(time.localtime()) - podaje czas w przyjemny sposób: ', time.asctime(time.localtime()))
print('------time.strftime("%Y/%m", licznik)) - string format podaje to co chcę (np. tylko rok/miesiąc) z podanej daty: ', time.strftime("%Y/%m:", licznik),'\n')


# można do niego wpisać %Y/%m/%d %H:%M:%S


print('-----------------NOWY SLAJD 3---------------------------------------------------')
# Funkcja time.strptime() parsuje łańcuch znaków i tworzy z niego krotkę z datą i czasem
import time
print('------time.strptime() - drukuje podany string w postaci daty:')
print(time.strptime(('4 03, 2023'), '%d %m, %Y'))


#Funkcja time.sleep usypia główny wątek programu na określoną ilość sekund + pomiar czasu
print('-----------------NOWY SLAJD 4---------------------------------------------------')
print('------ tStart = time.counter() - pomiar czasu start: ')
tStart = time.perf_counter()
print(type(tStart))
print('-----------------pętelka z usypianiem czasu time.sleep(0.1)---------------------------------------------------')
i = 0
while i < 10:
    time.sleep(0.1) # pauzuje program na 0.1 sekundy
    print(time.asctime(time.localtime()))
    i += 1


print('------ tEnd = time.counter() - pomiar czasu koniec: ')
tEnd = time.perf_counter()

print('Czas wykonywania programu a własciwie ostetniej linijki kodu wyniósł:', tEnd - tStart)


# Operacje na import datetime
import datetime
print('-----------------NOWY SLAJD 5---------------------------------------------------')

print('------datetimeObj = datetime.datetime(2023, 11, 9) drukuje nam piękną datę w <class ''datetime.datetime>: ', datetime.datetime(2023, 9, 20))
datetimeObj = datetime.datetime(2023, 11, 9, 17, 9, 55)
print('------ klasa tego, co na górze',type(datetimeObj), datetimeObj)



print('------datetimeObj.date() - drukuje nam date:', datetimeObj.date(), type(datetimeObj.date()))
print('------datetimeObj.time() - drukuje nam godzinę:', datetimeObj.time())
print('------datetimeObj.timestamp() - drukuje nam ile czasu mineło od 1970 do daty zapisanej w datetimeObj:', datetimeObj.timestamp())
print('------time.time() - mówi nam ile sekund minęło od POCZĄTKU' , time.time())
print('------datetimeObj.weekday() - mówi nam jaki jest dzień tygodnia w dateTimeObj - (liczymy od indeksu 0!)', datetimeObj.weekday())
print('------datetimeObj.today() - drukuje nam datę dzisiaj z mikrosekundami', datetimeObj.today())
print('------datetimeObj.year - drukuje nam rok (pamiętaj, że nie ma nawiasów w funkcji!):', datetimeObj.year)
print('------datetimeObj.hour - drukuje nam godzinę (pamiętaj, że nie ma nawiasów w funkcji!):', datetimeObj.hour)
print('------datetimeObj.minute - drukuje nam minutę (pamiętaj, że nie ma nawiasów w funkcji!):', datetimeObj.minute)
print('------datetimeObj.second - drukuje nam sekundy (pamiętaj, że nie ma nawiasów w funkcji!):', datetimeObj.second)
print('------datetimeObj.microsecond - drukuje nam microsekundy (pamiętaj, że nie ma nawiasów w funkcji!):', datetimeObj.microsecond)



print('-----------------NOWY SLAJD 6---------------------------------------------------')
print('------NA KONIEC TAKIE MIŁE LOGICZNE PORÓWNANIA')
datetime1 = datetime.datetime(2023, 5, 6, 20, 54, 12)
datetime2 = datetime.datetime(2023, 5, 6, 22, 54, 12)
print(datetime1 < datetime2)

print('------porównanie datetime1 < datetime2: ', datetime1 < datetime2, 'typ tego cuda: ', type(datetime1 < datetime2) )

date1 = datetime.date(2023, 5, 6)
date2 = datetime.date(2023, 5, 17)
print(date1 < date2)





