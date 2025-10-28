from grille import Grille

def test_init():
    grille_test=Grille()
    assert isinstance(grille_test,Grille)
    assert len(grille_test.grille) == 3, "Échec : Le nombre de lignes est incorrect."
    assert len(grille_test.grille[0]) == 3, "Échec : Le nombre de colonnes est incorrect."
    
    print("\n Test 'test_init' réussi : L'objet Grille a été créé avec succès.")
test_init()

print("Début test tir")

def test_tir():
    grille_test=Grille()
    grille_test.tirer(0,0)
    assert grille_test.grille[0][0] == 'x'
    grille_test.tirer(0,0)
    assert grille_test.grille[0][0] == 'x'
    assert grille_test.tirer(-1,0) == False

test_tir()

print("Fin test tir")  