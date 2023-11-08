# Lekcja - 80 return - cwiczenie.py

def sumListElements(list):
    if len(list) == 0:
        print("Empty List")
        return None
    
    result = 0
    for val in list:
        result += val
    return result

jeden = sumListElements([])
dwa = sumListElements([1,2,3,4,5])

print(jeden)
print(dwa)