class File:
    def __init__(self, taille):
        self.__taille = taille
        self.__L = [2, 2] + [None]*taille

    def est_vide(self):
        self.tete() == None

    def est_pleine(self):
        return self.queue() != None

    def tete(self):
        return self.__L[self.__L[0]]

    def queue(self):
        return self.__L[self.__L[1]]

    def enfiler(self, x):
        if self.est_pleine():
            print("C'est plein !")
        else:
            print(f"on enfine {x}")
            self.__L[self.__L[1]] = x
            self.__L[1] += 1
            if self.__L[1] >= self.__taille + 2:
                self.__L[1] = 2


    def defiler(self):
        if self.est_vide():
            print("c'est vide")
        else:
            tete = self.tete()
            self.__L[self.__L[0]] = None
            self.__L[0] += 1
            if self.__L[0] >= self.__taille +2:
                self.__L[0] = 2

            return tete

    def __repr__(self):
        return str(self.__L)