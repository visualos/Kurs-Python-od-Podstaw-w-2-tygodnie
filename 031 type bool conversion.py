# Lekcja 31 - Konwersje typów na Boolean - ćwiczenie

# falsy values
print( bool())
print( bool(0))
print( bool(0.0))
print( bool( () ))
print( bool( [] ))
print( bool( {} ))
print( bool(None))
print( bool(False))

# True values
print( bool(True))
print( bool(1))
print( bool(0.1))
print( bool(-10))
print( bool( (0,) ))# ciekawostka: po usunięciu przecinka będzie false, 
                    # ale jak wstawimy coś innego niż "0" to i tak będzie True
                    # czyli przecinek, mówi Pythonowi, że będzie coś więcej niż zero w krotce hmm...    
print( bool( [0] ))
print( bool( {1} ))
print( bool( "jakiś string" ))
