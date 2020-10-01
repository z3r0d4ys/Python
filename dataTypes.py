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

        Person.id += 1

    def kill(self):
        if self.isAlive:
            self.isAlive = False
            self.deathDate = datetime.datetime.now()
            return True

        return False

    def calculateAge(self):
        self.age = datetime.datetime.now().year - self.birthDate.year
