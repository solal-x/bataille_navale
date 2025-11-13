# User Story : "Plouf dans l'eau"
# Utilisateur : un joueur
# Story : On veut pouvoir gérer les tirs de l'adversaire
# Actions :
#   1. créer une grille à 5 lignes et 8 colonnes
#   2. afficher la grille à l'écran
#   3. demander à l'utilisateur de rentrer deux coordonnées x et y
#   4. tirer à l'endroit indiqué sur la grille
#   5. retour en 2

from grille import Grille

g = Grille(5, 8)
print(g)

while True:
    try:
        l = int(input("Entrez l (0..4) : "))
        c = int(input("Entrez c (0..7) : "))
    except ValueError:
        print("Coordonées invalide, recommencez")
        continue
    g.tirer(l, c)
    print(g)

