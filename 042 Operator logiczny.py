# 
"""
Operatory logiczne - umożliwiają zastosowanie wielu porównań w celu uzyskania jednej ostatecznej wartości 
True/False. Stosowane są powszechnie w konstrukcjach wartunkowych i pętlac.

and = true jeśli true + true
or = true jeśli chociaż jedna wartość jest prawdą
not = odwrócenie wartości logicznej

"""


# and
print(13 == 13 and 12 == 12) #True
print(9 == 13 and 12 == 12) #False

# or
print(13 == 13 or 12 == 12) #True
print(9 == 13 or 12 == 12) #True


# not 
print(not(13 == 13 and 12 == 12)) #True zamienia na False
print(not(9 == 13 and 12 == 12)) #False zamienia na True


