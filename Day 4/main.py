import re

validPassports = 0

with open("./Day 4/data.txt", "r") as input:
    amount = 0
    cidMiss = True

    for line in input:
        if not line.strip():
            if amount == 8 or (amount == 7 and cidMiss):
                print("found valid, amount = {}, and cidmiss is: {}".format(amount, cidMiss))
                validPassports += 1
            cidMiss = True
            amount = 0
            continue
        if re.search(r'cid:', line):
            cidMiss = False
        amount += len(line.split())
        print("line: " + line, end="")
        print("Found {} entries".format(len(line.split())))

print(validPassports)

        