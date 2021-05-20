import re

data = list()

with open("./Day 2/data.txt", "r") as input:
    for line in input:
        data.append(line)

def CheckValid(line):
    min = int(re.search(r'^[0-9]+', line).group(0))
    max = int(re.search(r'(?<=-)[0-9]+', line).group(0))
    character = re.search(r'\w(?=:)', line).group(0)
    password = re.search(r'(?<=: )\w+', line).group(0)
    amount = len(re.findall(character, password))
    if amount >= min and amount <= max:
        return True
    else:
        return False

amountValid = 0
for line in data:
    if CheckValid(line):
        amountValid += 1

print(amountValid)