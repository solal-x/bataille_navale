import random
from grille import Grille
from bateau import sous_marin, torpilleur, croiseur, porte_avion
import sys

NB_LIGNES = 8
NB_COLONNES = 10
CLASSES_A_PLACER = [porte_avion, croiseur, torpilleur, sous_marin] 


def initialiser_jeu(): 
    grille_de_jeu = Grille(NB_LIGNES, NB_COLONNES)
    liste_bateaux_places = []

    for BateauClass in CLASSES_A_PLACER:
        placement_reussi = False
        tentatives_max = 1000 
        tentative_actuelle = 0
        
        while not placement_reussi and tentative_actuelle < tentatives_max:
            ligne_rand = random.randint(0, NB_LIGNES - 1)
            colonne_rand = random.randint(0, NB_COLONNES - 1)
            vertical_rand = random.choice([True, False])
            bateau_temp = BateauClass(ligne_rand, colonne_rand, vertical=vertical_rand)
            placement_reussi = grille_de_jeu.ajoute(bateau_temp)
            tentative_actuelle += 1
            
        if placement_reussi:
            liste_bateaux_places.append(bateau_temp)
        else:
            print("ÉCHEC FATAL: Impossible de placer tous les bateaux.")
            sys.exit(1)

    print("Initialisation terminée. Prêt à jouer.")
    return grille_de_jeu, liste_bateaux_places

# --------------------------------------------------------------------------------

def jouer_partie(grille_du_jeu, bateaux_du_jeu):
    print("\n=============================================")
    print(" DÉBUT DE LA PARTIE ")
    print("=============================================")
    
    bateaux_restants = len(bateaux_du_jeu)
    tirs_totaux = 0
    
    while bateaux_restants > 0:
        print("\n--- GRILLE DE JEU ACTUELLE ---")
        grille_du_jeu.afficher()
        print(f"Bateaux restants: {bateaux_restants}")
        
        while True:
            entree = input(f"Entrez les coordonnées (LIGNE,COLONNE | ex: 0,{NB_COLONNES - 1}) : ").strip()
            
            if entree.lower() == 'quitter':
                print("Partie abandonnée.")
                return 
            
            try:
                if ',' not in entree:
                    raise ValueError
                    
                ligne, colonne = map(int, entree.split(','))
                
                if not (0 <= ligne < NB_LIGNES and 0 <= colonne < NB_COLONNES):
                    raise ValueError
                
                break 

            except ValueError:
                print("Format incorrect. Utilisez LIGNE,COLONNE avec des chiffres dans les limites de la grille.")
                
        tirs_totaux += 1
            
        grille_du_jeu.tirer(ligne, colonne)
        
        bateaux_restants = 0
        for bateau in bateaux_du_jeu:
            if not bateau.coulé(grille_du_jeu):
                bateaux_restants += 1
            
        if bateaux_restants == 0:
            break
            
    if bateaux_restants == 0:
        print("\n=============================================")
        print(f"VICTOIRE ! Tous les bateaux sont coulés en {tirs_totaux} tirs.")
        print("=============================================")
    
    grille_du_jeu.afficher()


##############################################################################################################################
grille_du_jeu, bateaux_du_jeu = initialiser_jeu()

if grille_du_jeu:
    jouer_partie(grille_du_jeu, bateaux_du_jeu)