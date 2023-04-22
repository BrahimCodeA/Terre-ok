
import sys

# Récupérer l'heure au format 12 heures depuis la ligne de commande
heure12 = sys.argv[1]

# Extraire l'heure et les minutes de l'argument
heure, minute = heure12[:-2].split(':')

# Ajouter 12 heures si l'heure est PM (après midi) sauf si c'est 12 PM qui correspond à midi
if heure12[-2:] == 'PM' and heure != '12':
    heure = str(int(heure) + 12)

# Retourner à minuit si l'heure est 12 AM qui correspond à minuit
if heure12[-2:] == 'AM' and heure == '12':
    heure = '00'

# Si l'heure est midi, convertir en 12:00
if heure12[-2:] == 'PM' and heure == '12':
    heure = '12'

# Afficher l'heure au format 24 heures
heure24 = f"{heure.zfill(2)}:{minute}"
print(heure24)
