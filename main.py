
from grille import Grille
from bateau import sous_marin, torpilleur, croiseur, porte_avion
import random

nombre_lignes, nombre_colonnes = 8, 10
Grille_de_jeu = Grille(nombre_lignes, nombre_colonnes)
Liste_bateaux = [sous_marin, torpilleur, croiseur, porte_avion]
longueur_bateaux = [4, 3, 2, 2] 

def lancer_jeu():
    Grille_de_jeu = Grille(8, 10)
    Liste_bateaux = [sous_marin, torpilleur, croiseur, porte_avion]
    for boat in Liste_bateaux:
        Grille_de_jeu.ajoute(boat)
        Liste_bateaux.pop(boat)
        for autre in Liste_bateaux:
            if boat.chevauchement(autre) == 0 or None:
                Grille_de_jeu.ajoute(autre)
    




def initialiser_jeu():  
    Grille_de_jeu = Grille(nombre_lignes, nombre_colonnes)
    Liste_bateaux = [sous_marin, torpilleur, croiseur, porte_avion]
    for BateauClass in Liste_bateaux:
        placement_reussi = False
        tentatives_max = 1000 
        tentative_actuelle = 0
        Liste_bateaux_places = []
        while not placement_reussi and tentative_actuelle < tentatives_max:
            ligne_rand = random.randint(0, nombre_lignes - 1)
            colonne_rand = random.randint(0, nombre_colonnes - 1)
            vertical_rand = random.choice([True, False])
            bateau_temp = BateauClass(ligne_rand, colonne_rand, vertical=vertical_rand)
            placement_reussi = Grille_de_jeu.ajoute(bateau_temp)
            tentative_actuelle += 1
            
        if placement_reussi:
            Liste_bateaux_places.append(bateau_temp)
        else:
            print(f"❌ ÉCHEC : Impossible de placer le bateau après {tentatives_max} tentatives.")
            return None, None 

    print("\n---------------------------------------------")
    
    return Grille_de_jeu, Liste_bateaux_places

# --- EXÉCUTION DU JEU ---
grille_du_jeu, bateaux_du_jeu = initialiser_jeu()

if grille_du_jeu:
    print("\nÉTAT FINAL DE LA GRILLE DU JOUEUR :")
    grille_du_jeu.afficher()