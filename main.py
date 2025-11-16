
from grille import Grille
from bateau import sous_marin, torpilleur, croiseur, porte_avion
import random


class Couleur:
    VIDE = '\033[94m'  
    BATEAU = '\033[92m' 
    TOUCHE = '\033[91m'  
    RATE = '\033[96m'  
    FIN = '\033[0m'    

nombre_lignes, nombre_colonnes = 8, 10
Grille_de_jeu = Grille(nombre_lignes, nombre_colonnes)
Liste_bateaux = [sous_marin, torpilleur, croiseur, porte_avion]
longueur_bateaux = [4, 3, 2, 2] 

def initialiser_jeu():  
    Grille_de_jeu = Grille(nombre_lignes, nombre_colonnes)
    Liste_bateaux = [sous_marin, torpilleur, croiseur, porte_avion]
    Liste_bateaux_places = []
    for BateauClass in Liste_bateaux:
        placement_reussi = False
        tentatives_max = 1000 
        tentative_actuelle = 0
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

import random
from grille import Grille
from bateau import sous_marin, torpilleur, croiseur, porte_avion
# Retrait de l'import re

# --- CONFIGURATION ---
NB_LIGNES = 8
NB_COLONNES = 10
CLASSES_A_PLACER = [porte_avion, croiseur, torpilleur, sous_marin] 

def initialiser_jeu(): 
    """Place les bateaux aléatoirement sur une grille 8x10 sans chevauchement."""
    
    grille_de_jeu = Grille(NB_LIGNES, NB_COLONNES)
    liste_bateaux_places = []
    
    # print(f"--- Initialisation d'une grille {NB_LIGNES}x{NB_COLONNES} ---")
    
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
            return None, None 

    print("✅ Initialisation terminée. Prêt à jouer.")
    return grille_de_jeu, liste_bateaux_places

# --------------------------------------------------------------------------------

def jouer_partie(grille_du_jeu, bateaux_du_jeu):
    """Contient la boucle principale du jeu (tirs et vérification) avec validation stricte."""
    
    print("\n=============================================")
    print("🎯 DÉBUT DE LA PARTIE 🎯")
    print("=============================================")
    
    bateaux_restants = len(bateaux_du_jeu)
    tirs_totaux = 0
    
    while bateaux_restants > 0:
        print("\n--- GRILLE DE JEU ACTUELLE ---")
        grille_du_jeu.afficher()
        print(f"Bateaux restants: {bateaux_restants}")
        

        while True:
           
            entree = input(f"Nouvelle tentative: Entrez les coordonnées (LIGNE,COLONNE | ex: 0,{NB_COLONNES - 1}) : ").strip()
            
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


grille_du_jeu, bateaux_du_jeu = initialiser_jeu()

if grille_du_jeu:
    jouer_partie(grille_du_jeu, bateaux_du_jeu)


