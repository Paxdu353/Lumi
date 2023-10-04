from math import gcd
import math
class Fraction:
    def __init__(self, a, b):
        self.numerateur = a // gcd(a, b)
        self.denominateur = b // gcd(a, b)
        self.compacte = self.numerateur/self.denominateur

        if b == 0:
            raise ZeroDivisionError("Pas de 0 au dénominateur !")


    def isdecimal(self):
        D = self.denominateur
        while D % 2 == 0:
            D //= 2

        while D % 5 == 0:
            D //= 5

        return D == 1



    def __repr__(self):
        return f'{self.numerateur}/{self.denominateur}'

    def __add__(self, nbr):
        if isinstance(nbr, int):
            NouvelleFraction = Fraction(self.numerateur + (self.denominateur * nbr), self.denominateur)
            return NouvelleFraction
        elif isinstance(nbr, Fraction):
            NouvelleFraction = Fraction(self.numerateur * nbr.denominateur + self.denominateur * nbr.numerateur, self.denominateur * nbr.denominateur)
            return NouvelleFraction
        else:
            raise TypeError(f"Opération impossible entre Fraction et {type(nbr)}")

    def __mul__(self, nbr):
        if isinstance(nbr, int):
            NouvelleFraction = Fraction(self.numerateur * nbr, self.denominateur)
            return NouvelleFraction
        elif isinstance(nbr, Fraction):
            NouvelleFraction = Fraction(self.numerateur * nbr.numerateur, self.denominateur * nbr.denominateur)
            return NouvelleFraction
        else:
            raise TypeError(f"Opération impossible entre Fraction et {type(nbr)}")

    def __pow__(self, pow):
        NouvelleFraction = Fraction(self.numerateur ** pow, self.denominateur ** pow)
        return NouvelleFraction

    def __rmul__(self, nbr):
        return self * nbr

    def __rpow__(self, pow):
        return self ** pow

    def __radd__(self, nbr):
        return self + nbr

    def __eq__(self, nbr):
        return

    def __ne__(self, other):
        pass


divise = Fraction(7, 8)

def float(nbr: Fraction = divise):
    return nbr.numerateur/nbr.denominateur

