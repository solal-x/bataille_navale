from grille import Grille
from bateau import Bateau


def test_init():
    grille_test = Grille()
    assert isinstance(grille_test, Grille)
    assert grille_test.lignes == 3, "Échec : Le nombre de lignes est incorrect."
    assert grille_test.colonnes == 3, "Échec : Le nombre de colonnes est incorrect."
    
    print("\n Test 'test_init' réussi : L'objet Grille a été créé avec succès.")


test_init()


print("Début test tir")


def test_tir():
    grille_test = Grille()
    grille_test.afficher()
    grille_test.tirer(0, 0)
    assert grille_test.grille[0][0] == 'x'
    grille_test.tirer(0, 0)
    assert grille_test.grille[0][0] == 'x'
    assert grille_test.tirer(-1, 0) == False
    grille_test.tirer(0,0)
    grille_test.afficher()

test_tir()
print("Fin test tir")

def test_ajout():
    print('début test_ajout')
    b1 = Bateau(0, 1, longueur=2)
    b2 = Bateau(1, 2, longueur=2, vertical=True)
    grille_test = Grille()
    grille_test.ajoute(b1)
    grille_test.ajoute(b2)
    grille_test.afficher()
    grille_test.tirer(1,2)
    b1.coulé(grille_test)
    b2.coulé(grille_test)
    grille_test.afficher()
    grille_test.tirer(2,2)
    b1.coulé(grille_test)
    b2.coulé(grille_test)
    grille_test.afficher()
    grille_test.tirer(0,2)
    b1.coulé(grille_test)
    grille_test.afficher()
    print("test_ajout réussi")

test_ajout()
