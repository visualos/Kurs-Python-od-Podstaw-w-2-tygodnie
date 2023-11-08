# Lekcja 54 - if elis else - ćwiczenie

n = 12 
if n >= 10:
    print("Ten warunek jest spełniony. Wartość n większa od 10")
    print("Ten warunek jest spełniony. Wartość n większa od 10!")

if n == 12:
    print("Ten warunek jest spełniony 12 = 12")


n = 7
if n == 10:
    print("n to 10")
elif n == 9:        # wykona tylko wtedy, kiedy pierwszy warunek nie będzie spełniony
    print("n to 9")
elif n == 8:
    print("n to 8")
elif n == 6:
    print("n to 6")
else: 
    print("W takim razie to żadna z powyższych liczb. Jest to,", n)


if 24 <= 100:
    print("wykona się")

if 24 <= 100: print("wykona się. To jest skrócony zapis. Działa tylko z jedną instrukcją")

# Zagnieżdżone sprawdzenia w instrukcji if
if 14 > 10:
    print("14 większe od 10")
    if 3 == 3:
        print("3 równe 3")
        if 12 < 90:
            print("12 mniejsze od 90")
