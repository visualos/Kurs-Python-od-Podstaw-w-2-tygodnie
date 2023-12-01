# Lekcja 101 Przydatne funckje do operacji na łańcuchach znaków - ćwiczenie.py

# String i find()
#1) Napisz funkcję validateEmail sprawdzającą w podstawowy
# sposób czy email jest prawidłowy.
# 2) Wykorzystaj find() do wyszukania fragmentów tekstu w email:
# sprawdź czy istnieje w przekazanym do funkcji emailu znak @, zapisz index w monkeyIndex
#
# - posiadając pozycję @ sprawdź czy istnieje znak kropki po małpie. Zapisz pozycję kropki w dotIndex
#
#
# jeżeli wszystkie powyższe warunki są spełnione zwróć True, w innym wypadku False
#
# 3) Wywołaj funkcję z następującymi mailami, pokaž w konsoli co zwraca funkcja:
#- asia@example.com
#-karol@domena
#-user.com
string1 = 'asia@example.com'
string2 = 'karol@domena.com'
string3 = 'user.com'
string4 = 'r.radek@italy.com'

def validateEmail(email):
    
    monkeyIndex =  email.find('@')
   
    secondIndex = email.rfind('.')
    if secondIndex > monkeyIndex and monkeyIndex > 0  :
        print(email)
        print(secondIndex)
    else:
        print("błędny email")
        print(secondIndex)



validateEmail(string1)
validateEmail(string2)
validateEmail(string3)
validateEmail(string4)



    
    