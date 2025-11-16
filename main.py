
from grille import Grille
from bateau import Bateau, sous_marin, torpilleur, croiseur, porte_avion

Grille_de_jeu = Grille(8, 10)
Liste_bateaux = [sous_marin, torpilleur, croiseur, porte_avion]

for boat in Liste_bateaux:
    Grille_de_jeu.ajoute(boat)
    Liste_bateaux.pop(boat)
    for autres in Liste_bateaux