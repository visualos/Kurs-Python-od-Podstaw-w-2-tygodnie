def filter_list(l):
    'return a new list with the strings filtered out'

    x =  list(filter(lambda x: not isinstance(x, str), l))
    print(x)



madox = [10, 11, 12, 13 ,14 , f'radek to misztrz']        
filter_list(madox)

print(f'radek {madox} jest najlepszy')

