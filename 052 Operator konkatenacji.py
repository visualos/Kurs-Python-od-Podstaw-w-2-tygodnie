# Lekcja 52 - Operator konkatenacji.

"""
Operator konkatenacji służy do łączenia łancuchów znaków, list, zbiorów itd.
"""

txt = "Cześć "
newTxt = txt + "Świecie"
print(newTxt)


numList = [10, 11, 12, 13, 14, 15]
newList = numList + [16, 17]
print(newList)

a = ("jeden", "dwa")
b = ("trzy",)
print(a + b)