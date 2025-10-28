import numpy as np
class Grille:
    vide = "~"
    
    def __init__(self, lignes=3, colonnes=3):
        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [[self.vide for i in range(self.colonnes)] 
                       for i in range(self.lignes)]
        
        

    def afficher(self):
        for ligne in self.grille:
            print(ligne)
    
    def tirer(self, ligne, colonne):
        if not (0 <= ligne < self.lignes and 0 <= colonne < self.colonnes):
            print("Tir hors limites de la grille.")
            return False
        G = self.grille
        case = G[ligne][colonne]
        if case == self.vide:
            self.grille[ligne][colonne] = 'x'
            print("raté")
        elif case == 'x':
            print("déjà tiré ici")
   