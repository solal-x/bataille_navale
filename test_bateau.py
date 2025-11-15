from bateau import Bateau
from grille import Grille

def test_init():
    ligne_test = 10
    colonne_test = 10
    b_test = Bateau(ligne_test, colonne_test)
    assert isinstance(b_test, Bateau)
    assert b_test.ligne == ligne_test
    assert b_test.colonne == colonne_test
    assert b_test.longueur == 1,  "Echec: La longueur par défaut est 1"
    print("test_init bateau réussi")

test_init()

def test_pos():
    b1 = Bateau(2, 3, longueur=3)
    b2 = Bateau(2, 3, longueur=3, vertical=True)
    attendu1 = [(2, 3), (2, 4), (2, 5)]
    attendu2 = [(2, 3), (3, 3), (4, 3)]
    obtenu1 = b1.positions
    obtenu2 = b2.positions
    assert obtenu1 == attendu1 and obtenu2 == attendu2
    print("test_pos réussi") 
    
test_pos()

def test_chev():
    b1 = Bateau(2, 3, longueur=3)
    b2 = Bateau(2, 3, longueur=3, vertical=True)
    assert b1.chevauchement(b2) == 1
    b3 = Bateau(3, 3, longueur=3, vertical=True)
    assert b1.chevauchement(b3) == 0
    print("test_chevauchement réussi")

test_chev()