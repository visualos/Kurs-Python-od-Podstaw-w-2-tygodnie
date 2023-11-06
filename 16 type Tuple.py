# Lekcja 16 - Typ tuple - krotka - ćwiczenie

users = ("Ania", "Karol", "Marta", "Adam") # bez nawiasów również stworzyłby <class 'tuple'>

#user[0] = "Paweł" # krotki nie można modyfikować, błąd
print(users)            #('Ania', 'Karol', 'Marta', 'Adam')
print(type(users))
print(len(users))


print(users[0])         # Ania
print(users[0][0])      # A
print(users[2][0])      # M