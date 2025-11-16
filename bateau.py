

class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    @property
    def positions(self):
        liste_pos = []
        if self.vertical:
            for i in range(self.longueur):
                liste_pos.append((self.ligne + i, self.colonne))
        else:
            for i in range(self.longueur):
                liste_pos.append((self.ligne, self.colonne + i))
        return liste_pos
    
    def chevauchement(self, autre_bateau):
        liste_chevauchements = []
        positions_self = set(self.positions)
        positions_autre = set(autre_bateau.positions)
        liste_chevauchements = positions_self.intersection(positions_autre)
        return len(liste_chevauchements) > 0
    
    def coulé(self, grille):
        emplacement = self.positions
        for ligne, colonne in emplacement:
            index = ligne * grille.colonnes + colonne
            degats = grille.grille[index]
            if degats != 'x':
                return False
        print('coulé !')
        return True
      

class porte_avion(Bateau):
    def __init__(self, ligne, colonne, longueur=4, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical)


class croiseur(Bateau):
    def __init__(self, ligne, colonne, longueur=3, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical)


class torpilleur(Bateau):
    def __init__(self, ligne, colonne, longueur=2, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)


class sous_marin(Bateau):
    def __init__(self, ligne, colonne, longueur=2, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
