# Lekcja 19 - Typ Dict - słownik


# Słownik to zbiór par kluczy oraz wartości. Klucze musza być unikatowe i służą do pobierania wartości. 
# Elementy w słowniku nie mają kolejności, nie jest to lista.

contacts = {
    "Ania" : "ania@example.com",
    "Daniel" : "daniel@example.com",
    "Ola" : "ola@example.com"
}

contacts["Olek"] = "olek@example.com"
print(len(contacts)) # 4
print(contacts["Ania"]) #"ania@example.com"
print(contacts["Daniel"]) #"daniel@example.com"

print(contacts.keys())  # klucze dostępu kontaktu
print(contacts.values()) # wartości dostępne w słowniku


print("Klucz dla wartości daniel@example(...) to: ", list(contacts.keys())[list(contacts.values()).index("daniel@example.com")])