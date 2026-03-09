# fontions
def CalCulerPerimetre(Longeur, Largeur):
    perimetre = 2 * (Longeur + Largeur)
    return perimetre

def CalculerAire(Longeur, Largeur):
    aire = Longeur * Largeur
    return aire

# afficher le carré

from exo3 import AffcherCarre

print("Le perimetre es ", CalCulerPerimetre(8,4))

AffcherCarre(8,4)