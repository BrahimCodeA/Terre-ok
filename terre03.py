import sys

# Recuperer la lettre choisi par l'utilisateur
lettre = sys.argv[1]

# Parcour les lettres de l'alphabet 
for c in range(ord(lettre), ord('z')+1):

# Affiche l'alphabet a partir de la lettre choisi par l'utilisateur
    print(chr(c), end='')

print()
