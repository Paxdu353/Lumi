import math

class PGCD:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def solve(self):
        return str(math.gcd(self.a, self.b))
    def simplify(self):
        if self.b != 0:
            print(self)
        else:
            print(f"{self} = {self.solve()}")
            return

        while self.b != 0:
            self.a, self.b = self.b, self.a % self.b
            if self.b != 0:
                print(self)
            else:
                print(f"{self} = {self.solve()}")
                return


    def __repr__(self):
        return f"PGCD({self.a} ; {self.b})"


def si(a, b):
    return PGCD(a, b).simplify()

def so(a, b):
    return PGCD(a, b).solve()