from grille import Grille

def test_init():
    grille_test=Grille()
    assert isinstance(grille_test,Grille)
    assert len(grille_test.grille) == 3, "Échec : Le nombre de lignes est incorrect."
    assert len(grille_test.grille[0]) == 3, "Échec : Le nombre de colonnes est incorrect."
    
    print("\n Test 'test_init' réussi : L'objet Grille a été créé avec succès.")
test_init()
