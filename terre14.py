
import sys

# Vérifier si un argument a été passée
if len(sys.argv) < 2:
    print("erreur .")
    sys.exit(1)

numbers = []
for arg in sys.argv[1:]:
    if not arg.isdigit():
        print(f"{arg} erreur.")
        sys.exit(1)
    numbers.append(int(arg))

# Vérifier si la liste est triée en utilisant un boucle
is_sorted = True
for i in range(1, len(numbers)):
    if numbers[i] < numbers[i-1]:
        is_sorted = False
        break
# Afficher Triée si la liste est triée sinon afficher Pas triée 
if is_sorted:
    print("Triée !")
else:
    print("Pas triée !")
