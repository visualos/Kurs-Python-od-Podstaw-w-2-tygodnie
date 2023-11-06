# Lekcja 21 - Dict test

"""
Wymagania:
1. Stwórz zmienną config, która będzie słownikiem
z konfiguracją strony internetowej, zapisz w niej
poniższe klucze z wartością:
    - "website" z wartością "example.com"
    - "dbType" z wartością "sql"
    - "dbUser" z wartością "admin123"
    - "dbPassword" z wartością "pass123"
2. Pokaż ilość elementów słownika w konsoli
3. Pokaż w konsoli wartość klucza "dbType" ze słownika
4. Wykorzystaj pętle for in, aby przejść po wszystkich
elementach słownika i pokaż je w konsoli według formatu:
    "Klucz w config: website z wartością example.com"

"""

config = {                                                          # tworzenie słownika
    "website": "example.com",
    "website2": "example.com",
    "dbType": "sql",
    "dbUser": "admin123",
    "dbPassword": "pass123"
}

print(len(config))                                                  # długość słownika
print(config["dbType"])                                             # podaje wartość dla klucza dbType

for key in config.keys():                                           
    print("Klucz config:", key, "z wartością", config[key])         # drukuje kompletną listę słownika z opisem

for key, value in config.items():
    print("Klucz config:", key, "z wartością", value)               # drukuje kompletną listę słownika z opisem (krótsza wersja)

print("nowa linia \n\n\n\n\n")                                      # drukuje klucze tylko dla wartości "example.com"
for key, value in config.items():
    if value == "example.com":
        print("Klucz config:", key, "z wartością", value)
        print("Klucz config:", key, "z wartością", value)