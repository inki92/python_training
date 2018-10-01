class Critter(object):
    def __init__(self, name):
        print("New!")
        self.name = name
    def __str__(self):
        rep = "Object from Critter class"
        rep += "Name is " + self.name + "\n"
        return rep
    def talk(self):
        print("Hello. My name is ", self.name, "\n")
crit1 = Critter("Bobik")
crit1.talk()
crit2 = Critter("Sharik")
crit2.talk()
print(crit1)
print(crit1.name)
