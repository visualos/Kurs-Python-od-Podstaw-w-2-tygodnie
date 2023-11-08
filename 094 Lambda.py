#Lekcja 94 Lambda.py


# Lambda, to taka funkcja, w krótkiej postaci

sumiczka = lambda a, b: a + b

print(sumiczka (4, 5))

# Można wrzucić lambdę do funkcji:

LAM = lambda x, y: x * y
print(LAM(4, 5))

print((lambda x, y: x * y)(5,6))

 

# Mamy jeszcze takie cudo jak map "()", które odpowiada za:
# Map Function = map(function, iterable)
#   - Returns an iterator that applies function to every item of iterable
# https://www.youtube.com/watch?v=8q2vICb89ys&ab_channel=b001 :
def make_even(num):
    if num%2==1:
        return num+1
    else:
        return num
x = [551, 641, 891, 122, 453, 223, 234, 343, 562, 115, 554, 111, 679, 516]
y = list(map(make_even, x))
print(y)    

# Jest JESZCZE JEDNO cudo, które nazywa się filter():
# Filter function - filter(function, iterable)
#                 - returs items from iterable based on some criteria

# Można powiedzieć, że ta funkcja filtruje np. słownik dzięki innej funkcji

listData = ["Ola", "Włodzimierz", "Kasia", "Izydor"]

# filtruje imiona, wybiera te które mają mniej niż 6 liter
result = filter (lambda x: len(x) <= 5, listData) # Output: [2, 4, 6]
print(list(result)) # ['Ola', 'Kasia']


# Jest jeszcze jedna funkcja z lambdą: Reduce ()

# Funkcja reduce redukuje selwencję do pojedynczej wartości:

from functools import reduce 

numSum = reduce((lambda x, y: x+y), [1, 2, 3, 4, 5])
print("Suma liczb:", numSum)





