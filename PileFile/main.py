import PileFile.File as F
import PileFile.Pile as P
import math as M
test = ""



def parenthesage(calc: str):
    if type(calc) != str: raise TypeError("Erreur de type")
    if calc.count("(") != calc.count(")"): raise Exception("Pas le meme nombre de parenthese")
    pile = P.Pile(calc.count("("))
    liste = []
    for (i, j) in enumerate(calc):
        if j == "(":
            pile.empiler(i)
        elif j == ")":
            if pile.est_vide():
                return False
            else:
                liste.append((pile.depiler(), i))

    return liste


def calcul_npi(liste : list):
    pass



