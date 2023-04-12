import sys

# Si aucun n'argument n'est donné alors on affichera une erreur
if len(sys.argv) != 2:
     print("erreur .")
     sys.exit(1)

# Récupérer la chaine de caractère passée en argument
chaine = sys.argv[1]

# Si l'argument entré est un nombre on affichera une erreur
if chaine.isdigit():
    print("erreur .")
    sys.exit(1)

# Compter le nombre de caractere
caracteres = len(chaine)

 # Afficher le nombre de caractere
print(caracteres)
