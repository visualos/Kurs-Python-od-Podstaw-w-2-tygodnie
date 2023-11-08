# Lekcja 24 - Typ Set i Frozenset - zadanie

'''
1. Stwórz set z unikalnymi wartościami jak:
    Toyota, Honda, BMW, Mercedes, Audi, Ford
2. Dodaj do set za pomocą funkcji add kolejne elementy:
    Volkswagen, Mazda, BMW, Mercedes, Audi, Chevrolet
3. Pokaż w konsoli wielkość set
4. Wykorzystaj pętlę for aby pokazać elementy set

'''
#1
unikalnySet = {"Toyota", "Honda", "BMW", "Mercedes", "Audi", "Ford"}
#2
unikalnySet.add("Volkswagen")
unikalnySet.add("Mazda")
unikalnySet.add("BMW")
unikalnySet.add("Mercedes")
unikalnySet.add("Audi")
unikalnySet.add("Chevrolet")
#3
print(len(unikalnySet))
#4
for value in unikalnySet:
    print(value)

