import sys
sys.setrecursionlimit(10000)

def puissance(x, n):
    if n == 1:
        return x
    else:
        return x * puissance(x, n-1)

def puissance_opti(x, n):
    if n == 1:
        return x
    else:
        if n % 2 == 0:
            return puissance_opti(x**2, n/2)
        else:
            return x * puissance_opti(x**2, (n-1)/2)


def mini(liste):
    min = liste[0]
    for i in liste[1:]:
        if i < min:
            min = i

    return min


def minimum(liste, debut = 0, fin = -1):
    if fin == -1:
        fin = len(liste) - 1
    if debut == fin:
        return liste[debut]
    else:
        milieu = (debut + fin) // 2
        x = minimum(liste, debut, milieu)
        y = minimum(liste, milieu + 1 , fin)

        if x < y:
            return x
        else:
            return  y
