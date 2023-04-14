
import sys

# On creer une boucle for qui verifie si il y a un autre diviseur que 1 et de lui même si c'est le cas le nombre n'est pas premier
def nombre_premier(nombre):
    if nombre <= 1:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    return True

# Si aucun n'argument n'est passé alors on affichera une erreur .
if len(sys.argv) < 2:
    print("erreur .")
    sys.exit(1)

# Si l'argument donné n'est pas un nombre on affichera un message d'erreur
if not sys.argv[1].isdigit():
    print("erreur .")
    sys.exit(1)

# Demande à l'utilisateur d'entrer un nombre
nombre = int(sys.argv[1])

# Appelle la fonction  pour vérifier si le nombre est premier 
# On affiche si le nombre est premier ou non avec la méthode f-string
if nombre_premier(nombre):
    print(f"Oui,", nombre, "est un nombre premier.")
else:
    print(f"Non,", nombre, "n'est pas un nombre premier.")

        
        