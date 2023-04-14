
import sys

# On import le module sys puis on verifie si un argument est entré si non on affichera un message d'erreur
if len(sys.argv) < 2:
    print("erreur .")
    sys.exit(1)
# Si l'argument donné n'est pas un nombre entier on affichera un message d'erreur
if not sys.argv[1].isdigit():
    print("erreur .")
    sys.exit(1)
# On converti la valeur de l'argument en nombre entier et on calcul la racine carré de l'argument
nombre = int(sys.argv[1]) 
resultat = int(nombre ** 0.5)  
# On affiche le resultat de la racine carré
print(resultat)
