import re

data = list()

with open("./Day 2/data.txt", "r") as input:
    for line in input:
        data.append(line)

def ParseLine(line):
    first = int(re.search(r'^[0-9]+', line).group(0))
    second = int(re.search(r'(?<=-)[0-9]+', line).group(0))
    character = re.search(r'\w(?=:)', line).group(0)
    password = re.search(r'(?<=: )\w+', line).group(0)
    return (first, second, character, password)

# Part 1

def CheckValid1(min, max, character, password):
    amount = len(re.findall(character, password))
    if amount >= min and amount <= max:
        return True
    else:
        return False

# Part 2

def CheckValid2(first, second, character, password):
    valid = False
    if password[first-1] == character:
        valid = not valid
    if password[second - 1] == character:
        valid = not valid
    return valid

amountValid1 = 0
amountValid2 = 0
for line in data:
    (first, second, character, password) = ParseLine(line)
    if CheckValid1(first, second, character, password):
        amountValid1 += 1
    if CheckValid2(first, second, character, password):
        amountValid2 += 1
