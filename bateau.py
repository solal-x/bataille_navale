class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def positions():
        liste_pos = []
        if self.vertical:
            for i in range(self.longueur):
                liste_pos.append(self.ligne + i, self.colonne)
        else:
            for i in range(self.longueur):
                liste_pos.append(self.ligne, self.colonne + i)
        return liste_pos
    