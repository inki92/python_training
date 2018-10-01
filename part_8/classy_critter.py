class Critter(object):
    total = 0
    @staticmethod
    def status():
        print("All ", Critter.total)
    def __init__(self, name):
        print("New!")
        self.name = name
        Critter.total += 1
print(Critter.total)
crit1 = Critter("One")
crit2 = Critter("Two")
crit3 = Critter("three")
Critter.status()
print(crit1.total)
