import random
from typing import List, Tuple
import os
from grille import Grille
from bateau import sous_marin, torpilleur, croiseur, porte_avion



class Couleur:
    VIDE = '\033[94m' 
    BATEAU = '\033[92m' 
    TOUCHE = '\033[91m' 
    RATE = '\033[96m' 
    FIN = '\033[0m' 
    
NB_LIGNES = 8
NB_COLONNES = 10
CLASSES_A_PLACER = [porte_avion, croiseur, torpilleur, sous_marin] 

def display_grid(grid: Grille, masque_tirs: bool) -> List[str]:
    
    output = []
    
    col_nums = "  " + " ".join([str(i) for i in range(grid.colonnes)])
    output.append(col_nums)
    
    for r in range(grid.lignes):
        
        row_str = f"{r} " 
        
        for c in range(grid.colonnes):
            
            etat = grid.etat(r, c)
            symbol = etat
            couleur = Couleur.FIN
            
            if etat == '~':
                symbol = '~'
                couleur = Couleur.VIDE
            elif etat == 'o':
                symbol = 'o'
                couleur = Couleur.BATEAU
                if masque_tirs:
                    symbol = '~'
                    couleur = Couleur.VIDE
            elif etat == 'x':
                symbol = 'X'
                couleur = Couleur.TOUCHE
            
            row_str += f"{couleur}{symbol}{Couleur.FIN} "
        output.append(row_str)
        
    return output

def afficher_grille_console(grille: Grille, titre: str, masque_tirs: bool):
    print(f"\n--- {titre} ---")
    grid_lines = display_grid(grille, masque_tirs=masque_tirs)
    for line in grid_lines:
        print(line)

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
            print("❌ Échec de l'initialisation : Trop de tentatives pour placer les bateaux.")
            return None, None 

    print("✅ Initialisation terminée. Prêt à jouer.")
    return grille_de_jeu, liste_bateaux_places

def jouer_partie(grille_du_jeu, bateaux_du_jeu):
    
    if 'os' in globals() and os.name != 'nt':
        os.system('clear')
    elif 'os' in globals() and os.name == 'nt':
        os.system('cls')
    
    print("\n=============================================")
    print("🎯 DÉBUT DE LA PARTIE 🎯")
    print("=============================================")
    
    bateaux_restants = len(bateaux_du_jeu)
    tirs_totaux = 0
    
    message_tour_precedent = ""
    
    while bateaux_restants > 0:
        
        if 'os' in globals():
            if os.name != 'nt': os.system('clear')
            else: os.system('cls')

        if message_tour_precedent:
            print(f"\n<<< RÉSULTAT DU TOUR PRÉCÉDENT >>>\n{message_tour_precedent}\n")
            message_tour_precedent = ""

        afficher_grille_console(grille_du_jeu, "GRILLE ENNEMIE (Vos Tirs)", masque_tirs=True)
        
        print(f"\nBateaux restants: {bateaux_restants}")
        
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

        etat_avant_tir = grille_du_jeu.etat(ligne, colonne)
        grille_du_jeu.tirer(ligne, colonne)
        etat_apres_tir = grille_du_jeu.etat(ligne, colonne)
        
        if etat_avant_tir == 'o' and etat_apres_tir == 'x':
            message_tour_precedent += "💥 TOUCHÉ !\n"
        elif etat_avant_tir == '~' and etat_apres_tir == 'o':
            message_tour_precedent += "💧 RATÉ !\n"
        elif etat_avant_tir == 'x' or etat_avant_tir == 'o':
             message_tour_precedent += "💡 Déjà tiré ici.\n"
        else:
            message_tour_precedent += "💧 RATÉ\n"
        
        nouveaux_bateaux_restants = 0
        for bateau in bateaux_du_jeu:
            
            est_coule_maintenant = bateau.coulé(grille_du_jeu)
            etait_coule_avant = getattr(bateau, 'est_coule_precedent', False)

            if not est_coule_maintenant:
                nouveaux_bateaux_restants += 1
            
            elif est_coule_maintenant and not etait_coule_avant:
                nom_bateau = type(bateau).__name__.replace('_', ' ').title()
                message_tour_precedent += f"💣 {Couleur.TOUCHE}Vous avez coulé le {nom_bateau} !{Couleur.FIN}\n"
                setattr(bateau, 'est_coule_precedent', True)

        bateaux_restants = nouveaux_bateaux_restants
        
        if bateaux_restants == 0:
            break
            
    if 'os' in globals():
        if os.name != 'nt': os.system('clear')
        else: os.system('cls')

    if bateaux_restants == 0:
        print("\n=============================================")
        print(f"🎉 {Couleur.BATEAU}VICTOIRE ! Tous les bateaux sont coulés en {tirs_totaux} tirs.{Couleur.FIN}")
        print("=============================================")
    
    afficher_grille_console(grille_du_jeu, "GRILLE FINALE (Complète)", masque_tirs=False)


if __name__ == "__main__":
    grille_du_jeu, bateaux_du_jeu = initialiser_jeu()

    if grille_du_jeu and bateaux_du_jeu:
        afficher_grille_console(grille_du_jeu, "VOTRE FLOTTE (Placement initial)", masque_tirs=False)
        input("\nAppuyez sur Entrée pour commencer la partie...")
        jouer_partie(grille_du_jeu, bateaux_du_jeu)
    else:
        print("Le jeu n'a pas pu être initialisé correctement.")