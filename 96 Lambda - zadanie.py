# Lekcja 96 - Lambda - zadanie.py

# Zadanie z lambdą i map
# 1) Stwórz listę names z wartościami: ola, Ania, Kasia
# 2) z pomocą mapy i lambdy dodaj do każdego imienia tekst" Kowalska"
# 3) Wyświetl nową listę w konsoli
# 4) Przefiltruj nową listę ze względu na długość tekstu, zachowaj
# w nowej liście tylko te które mają więcej niż 12 znaków
# Pokaż przefiltrowaną listę w konsoli

#1
names = ["Ola", "Ania", "Kasia"]

ppl = map(lambda x: x + " Kowalska", names)
ppl = list(ppl)
print(list(ppl))

#2 filter 
filtered = filter(lambda x: len(x) > 12, ppl)
print(list(filtered))
