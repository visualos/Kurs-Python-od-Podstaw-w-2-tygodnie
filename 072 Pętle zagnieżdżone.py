# Lekcja 72 - Pętle zagnieżdżone

"""
Python pozwala na zagnieżdżone pętle
"""

i = 0
while( i < 3 ):
    strData = " kupa "
    j = 0
    while( j < 3 ):
        strData += " dupa " + str(j)
        j += 1
    print(strData)
    i += 1