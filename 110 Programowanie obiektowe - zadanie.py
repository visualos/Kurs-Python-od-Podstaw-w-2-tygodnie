# Lekcja 110 - Programowanie obiektowe - zadanie

# Stwórz klasę PhoneSimCard reprezentującą kartę sim telefonu z kontaktami
# 1) Klasa PhoneSimCard tworzy atrybut/zmienną klasy phoneContacts jako listę w konstruktorze
# 2) Dodaj metodę addPhoneContact przyjmującą oprócz self również parametry
# contactName i phoneNumber. Sprawdź z funkcją isinstance czy przekazane dane są
# prawidłowe, czyli str i int. Stwórz słownik z contactName i phoneNumber i dodaj go
# do listy kontaktów obiektu powstałego na bazie klasy
# 3) Napisz metodę displayContacts, która w pętli pokaże kolejne kontakty w terminalu
# 4) Stwórz instancję klasy PhoneSimCard
# 5) Dodaj poniższe kontakty:
# "Ela", 987654321
# "Tomasz", 12345678
# - 200, 12345678
# A "Marta", "numer"
# Część danych jest nieprawidłowa, więc nie powinny być dodane przez addPhoneContact
# 6) Wyświetl kontakty z displayContacts()

class PhoneSimCard:

    def __init__(self):
        self.phoneContacts = []

    def addPhoneContact(self, contactName, phoneNumber):    
        if not isinstance (contactName, str) : return False
        if not isinstance (phoneNumber, int) : return False
    
        contact = {
            'contactName' : contactName,
            'phoneNumber' : phoneNumber
        }      

        self.phoneContacts.append(contact)
        

    def displayContacts(self):
        for contact in self.phoneContacts:
            print(contact['contactName'],' ', contact['phoneNumber'] )


phoneSim = PhoneSimCard()

phoneSim.addPhoneContact('Ela', 9283749238)
phoneSim.addPhoneContact('Tomasz', 98237423)
phoneSim.addPhoneContact(200, 23432)
phoneSim.addPhoneContact('radek', 'radek')

phoneSim.displayContacts()

PhoneSimCard().addPhoneContact('Ela', 9283749238)
PhoneSimCard().displayContacts()




        