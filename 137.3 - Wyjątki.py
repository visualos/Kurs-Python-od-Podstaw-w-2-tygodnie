# Lekcja 137.2 - Wyjątki.py

# Obsługa wyjątków - wywołanie wyjątku

num = 10

try:
    if num > 0:
        raise Exception("Exepction info")
        """
        funkcja raise w Pythonie jest wbudowanym mechanizmem do zgłaszania wyjątków. 
        Jest to konstrukcja językowa, która pozwala programiście na ręczne zgłaszanie wyjątków w określonych sytuacjach.
        """
    
  
except:
    print("Excepcion handled")
    
    """
    print("Excepcion handled"): 
    W bloku except znajduje się polecenie print, które wypisuje komunikat "Excepcion handled". 
    Oznacza to, że blok except obsługuje (łapie) dowolny wyjątek zgłoszony w bloku try i wyświetla 
    określony komunikat w przypadku jego wystąpienia.
    """