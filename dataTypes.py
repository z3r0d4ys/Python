import datetime


class Person:
    id = 0

    def __init__(self, name):
        self.name = name
        self.age = 0
        self.id = Person.id

        self.birthDate = datetime.datetime.now()
        self.deathDate = None

        self.isAlive = True

        self.isMarried = False

        Person.id += 1

    def kill(self):
        if self.isAlive:
            self.isAlive = False
            self.deathDate = datetime.datetime.now()
            return True

        return False

    def calculateAge(self):
        self.age = datetime.datetime.now().year - self.birthDate.year

    def __add__(self, other):
        if (not self.isMarried) and (not other.isMarried):
            return Family(self,other)
        else:
            return None


class Family:
    id = 0

    def __init__(self, groom, bride):
        self.id = Family.id
        Family.id += 1

        self.children = []
        self.woman = bride
        self.man = groom

        self.woman.isMarried = True
        self.man.isMarried = True

    def addChild(self, name):
        child = Person(name)
        self.children.append(child)


P1 = Person("John")
P2 = Person("Claire")

F1 = Family(P1, P2)
F2 = P1 + P2


