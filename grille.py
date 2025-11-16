import random
from bateau import Bateau

class Grille:
    vide = "~"
    
    def __init__(self, lignes=3, colonnes=3):
        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [self.vide for i in range(self.colonnes*self.lignes)]

    def afficher(self):
        for i in range(0, len(self.grille), self.colonnes):
            ligne = self.grille[i: i + self.colonnes]
            print(" ".join(ligne))
    
    def tirer(self, ligne, colonne, touche='x'):
        if not (0 <= ligne < self.lignes and 0 <= colonne < self.colonnes):
            print("Tir hors limites de la grille.")
            return False
        if (ligne in range(0, self.lignes)) and (colonne in range(0, self.colonnes)):

            G = self.grille
            coordo = ligne*self.colonnes + colonne
            case = G[coordo]
            if case == self.vide:
                self.grille[coordo] = touche
                print("raté")
            elif case == touche:
                print("déjà tiré ici")
            elif case == 'o':
                self.grille[coordo] = touche
                print('touché !')
   
    def ajoute(self, bateau):
        for (ligne, colonne) in bateau.positions:
            if not (0 <= ligne < self.lignes and 0 <= colonne < self.colonnes):
                return False
            if self.grille[ligne*self.colonnes + colonne] != self.vide:
                return False
        for (ligne, colonne) in bateau.positions:
            self.grille[ligne*self.colonnes + colonne] = "o"
        return True     
   