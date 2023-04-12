import sys

# Si aucun argument n'est passé on affichera un message d'erreur
if len(sys.argv) < 3:
    print("erreur .")
    sys.exit(1)

# Convertir les arguments qui passeront en nombre puis calculer la puissance du nombre choisi
nombre = int(sys.argv[1])
exposant = int(sys.argv[2])
resultat = nombre ** exposant

# Si l'exposant est inférieur à 0 donc négatif on affichera un message d'erreur
if exposant < 0:
    print("erreur .")

# Autrement on affichera le resultat de la puissance du nombre chosis
else:
    print(resultat)
    
