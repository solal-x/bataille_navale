class Grille:
    vide = "~"
    
    def __init__(self, lignes=3, colonnes=3):
        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [self.vide for i in range(self.colonnes*self.lignes)]

    def afficher(self):
        for ligne in self.grille:
            print(ligne)
    
    def tirer(self, ligne, colonne):
        if not (0 <= ligne < self.lignes and 0 <= colonne < self.colonnes):
            print("Tir hors limites de la grille.")
            return False
        if (ligne in range(0, self.lignes)) and (colonne in range(0, self.colonnes)):

            G = self.grille
            coordo = ligne*self.colonnes + colonne
            case = G[coordo]
            if case == self.vide:
                self.grille[coordo] = 'x'
                print("raté")
            elif case == 'x':
                print("déjà tiré ici")
   