
import sys

# Obtenez la chaine d'entrée à partir des arguments de la ligne de commande
chaine = sys.argv[1]

# Séparez les heures et les minutes
heure, minute = chaine.split(':')

# Changer les types des variables d'heure et de minute en entiers
heure = int(heure)
minute = int(minute)

# Vérifiez si l'heure est supérieure à 12 pour déterminer s'il s'agit de AM ou PM
temps = 'PM' if heure > 12 else 'AM'

# Afficher la chaine de temps formatée
print("{0}:{1:02d} {2}".format(heure % 12, minute, temps))

    
    