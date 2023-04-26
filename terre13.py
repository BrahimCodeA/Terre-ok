
import sys

nombre1 = int(sys.argv[1])
nombre2 = int(sys.argv[2])
nombre3 = int(sys.argv[3])

if nombre1 == nombre2 == nombre3:
    print("erreur.")
else:
    plus_petit = nombre1
    plus_grand = nombre1
    
    if nombre2 < plus_petit:
        plus_petit = nombre2
    
    elif nombre2 > plus_grand:
        plus_grand = nombre2
        
    if nombre3 < plus_petit:
        plus_petit = nombre3
    
    elif nombre3 > plus_grand:
        plus_grand = nombre3
    
    milieu = nombre1 + nombre2 + nombre3 - plus_petit - plus_grand
    print(milieu)



