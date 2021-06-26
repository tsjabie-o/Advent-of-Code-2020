raw_data = list()

with open("data.txt") as data:
    for line in data:
        raw_data.append(line)

class Suitcase:
    def __init__(self, colour):
        self.colour = colour
        self.parents = []
        self.children = []

    def AddParent(self, parent):
        self.parents.append(parent)

    def AddChild(self, child, amount):
        self.children.append((child, amount))

class SuitcaseTree():
    def __init__(self):
        self.suitcases = dict()

    def AddSuitcase(self, colour):
        if colour not in self.suitcases:
            suitcase = Suitcase(colour)
            self.suitcases[colour] = suitcase
        
    def AddChild(self, parentcolour, childcolour, amount):
        if childcolour not in self.suitcases:
            suitcase = Suitcase(childcolour)
            self.suitcases[childcolour] = suitcase
        self.suitcases[parentcolour].AddChild(childcolour, amount)
        self.suitcases[childcolour].AddParent(parentcolour)


suitcasetree = SuitcaseTree()

for line in raw_data:
    parentcolour = " ".join(line.split()[0:2])
    suitcasetree.AddSuitcase(parentcolour)

    childinfo = line.split("contain")[1].split(",")
    for child in childinfo:
        amount = child.split()[0]
        childcolour = " ".join(child.split()[1:3])
        suitcasetree.AddChild(parentcolour, childcolour, amount)


print(suitcasetree.suitcases["clear purple"].children)