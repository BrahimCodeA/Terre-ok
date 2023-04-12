import sys

# On verifie que la longueur des arguments est supérieur à 1
if (len(sys.argv)) >= 1:
 print(sys.argv)

# On extrait le deuxiéme argument de la ligne puis on l'inverse avec le Slicing
chaine = sys.argv[1][::-1]
print(chaine)
