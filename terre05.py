import sys

# Si aucun n'argument n'est passé alors on affichera un message d'erreur
if len(sys.argv) < 3:
  print("erreur.")
  sys.exit()

# On change le type des arguments qui seront passé pour pouvoir les diviser 
nombre1 = int(sys.argv[1])
nombre2 = int(sys.argv[2])

if nombre2 == 0:
     print("erreur.")
     sys.exit(1)
# Si le deuxiéme nombre est plus grand que le premier nombre alors on affichera erreur
if nombre1 < nombre2:
  print("erreur")
# Autrement on divisera les deux nombres passé en argument et on récupera le reste grace a l'operateur modulo
else:
  resultat = nombre1 // nombre2
  reste = nombre1 % nombre2
# Et on affichera le resultat et le reste de la divison avec f string
  print(f"Résultat: {resultat}")
  print(f"Reste: {reste}")
