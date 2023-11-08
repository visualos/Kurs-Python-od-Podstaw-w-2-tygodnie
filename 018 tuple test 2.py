# Lekcja 18 - Typ Tuple - zadnie 2

#1 Stwórz krotkę lastExpenses z ostatnimi wydatkami na koncie bankowym z wartościami: 200, 300, 400, 500, 600
#2 Policz wydatki z pomocą pętli for i wyświetl w konsoli ostateczną kwotę. Pamiętaj aby stworzyć z zmienną 
#   z wartośćią początkową 0 do której dodasz kolejny wydatek.



lastExpenses = 200, 300, 400, 500, 600
sum = 0
for value in lastExpenses:
    print(value)
    sum = sum + value
  

print("Suma wydatków:", sum)