# Lekcja 58 - if else i skrócony zapis porównania z wartością logiczną - ćwiczenia


status = True
if status == True:
    print("jest prawdziwy")

# niezalecane
if status is True:
    print("is True")

if status:
    print("prawda")

status = False

if status != True:  
    print("false")
if status is not True:
    print("false")
if not status:
    print("fałsz")