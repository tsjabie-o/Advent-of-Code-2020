from queue import Queue

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

    def FindAllParents(self, colour):
        foundparents = list()
        parentsToCheck = Queue()
        currentparents = self.suitcases[colour].parents
        if type(currentparents) is list:
            for parent in currentparents:
                parentsToCheck.put(parent)
        else:
            parentsToCheck.put(currentparents)

        while parentsToCheck.qsize() > 0:
            current = parentsToCheck.get()
            if current not in foundparents: foundparents.append(current)
            currentparents = self.suitcases[current].parents
            if type(currentparents) is list:
                for parent in currentparents:
                    parentsToCheck.put(parent)
            else:
                parentsToCheck.put(currentparents)
        return foundparents




suitcasetree = SuitcaseTree()

for line in raw_data:
    parentcolour = " ".join(line.split()[0:2])
    suitcasetree.AddSuitcase(parentcolour)

    childinfo = line.split("contain")[1].split(",")
    for child in childinfo:
        if "other" in child:
            continue
        amount = child.split()[0]
        childcolour = " ".join(child.split()[1:3])
        suitcasetree.AddChild(parentcolour, childcolour, amount)


print(len(suitcasetree.FindAllParents("shiny gold")))