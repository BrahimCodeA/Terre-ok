# Creez une variable qui stockera l'alphabet
alphabet = ''
# Creez une boucle qui parcourera les valeurs de ASCII avec la fonction ord
for lettre in range(ord('a'), ord('z')+1):
    alphabet += chr(lettre) + ''
# Afficher l'alphabet en minuscule
print(alphabet)

