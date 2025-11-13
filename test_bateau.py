from bateau import Bateau

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
    assert Bateau(2, 3, longueur=3).positions() == [(2, 3), (2, 4), (2, 5)]
    Bateau(2, 3, longueur=3, vertical=True).positions() == [(2, 3), (3, 3), (4, 3)]
    