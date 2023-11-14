# Lekcja 112 - Konstruktor ćwiczenie.py

                        
class Magazine:
    def __init__(self, author, title = 'unknown', isbn = 'unknown', year = 'unknown'):
        self.author = author
        self.title = title
        self.isbn = isbn
        self.year = year

    def displayData(self):
        print(self.title, self.author, self.isbn, self.year)

magazine1 = Magazine("radoslaw", "co burczy w brzuchach mrówek", 12341234 , 2005)
magazine1.displayData()