# Lekcja 74 - break continue pass

# Kontrola przebiegu pętli - break 
# Instrucja break przerywa działanie pętli i program kontynuuje swoją pracę za pętlą

dataArray = [0,1,2,3,4,5,6,7,8]

for value in dataArray:
    if value == 4:
        break # O TO CHODZI
    print(value)

print("KOOONIEC")

dataArray = [0,1,2,3,4,5,6,7,8]

for value in dataArray:
    if value == 4:
        continue # O TO CHODZI, przerywa tylko na == 4. Pętla leci dalej
    print(value)

print("KOOONIEC")


if 40 > 6:
    pass # O TO CHODZI, ona nic nie robi. Pusty wypełniacz. Stosuje się ją tam gdzie wymaga się jakiegoś kodu 
            # (np. na początku pisania programu jak nie wiemy co tam jeszcze będzie)
else:
    pass
print("KOOONIEC")
