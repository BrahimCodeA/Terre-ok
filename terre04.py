import sys
# Si aucun n'argument n'a été passé un message d'erreur s'affichera
if len(sys.argv) < 2:
    print("Tu ne me la mettras pas à l'envers .")
else:
# Autrement on verifira si l'argument est un nombre pair ou impair
 if sys.argv[1].isdigit():
    sys.argv[1] = int(sys.argv[1])
    nombre = sys.argv[1] % 2    
 # Si il est pair alors on affichera le message pair sinon on affichera qu'il est impair      
    if nombre == 0:
        print("pair")
    else:
        print("impair")
# Et si ce n'est pas un nombre mais des caractéres qui sont passé alors on affichera un message d'erreur
 else:
    print("Tu ne me la mettras pas à l'envers .")
