import time
class Pile:

    def __init__(self, taille):
        self.__taille = taille
        self.__L = [0] + [None] * taille

    def sommet(self):
        return self.__L[self.__L[0]]


    def empiler(self, number):
        if self.__L[0] != self.__taille:
            self.__L[0] += 1
            self.__L[self.__L[0]] = number
        else:
            print("Pile pleine")

    def depiler(self):
        if self.__L[1] != None:
            depile = self.sommet()
            self.__L[self.__L[0]] = None
            self.__L[0] -= 1
            return depile
        else:
            print("pile vide")

    def vider(self):
        T = time.time()
        listeRetour=[]
        while not self.est_vide():
            listeRetour.append(self.depiler())
        print(time.time() - T)
        return listeRetour


    def est_vide(self):
        return self.__L[0] == 0

    def est_pleine(self):
        return self.__L[0] == self.__taille

    def initialiser(self, N):
        self.__L = [0] + [None] * N

    def __repr__(self):
        return str(self.__L)


