class Grille:
    vide = "~"
    def __init__(self, lignes=3, colonnes=3):
        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [[ self.vide for i in range(self.colonnes)] for i in range(self.lignes)]

    def afficher(self):
        for ligne in self.grille:
            print(ligne)
    
    def tirer(ligne, colonne):
        if Grille[ligne*self.colonnes][colonne]==self.vide
            Grille[ligne*self.colonnes][colonne]="x"
            print("raté")
        if Grille[ligne*self.colonnes][colonne]=="x":
            print("déjà tiré ici")
        