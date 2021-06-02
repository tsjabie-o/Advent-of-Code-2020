passports = list()

with open("./Day 4/data.txt", "r") as inpt:
    data = inpt.read()

lines = data.split("\n\n")
lines = [line.replace("\n", " ") for line in lines]

passports = list()

for line in lines:
    passport = dict()
    fields = line.split()
    for field in fields:
        key, value = field.split(":")
        passport[key] = value
    passports.append(passport)

validPassports = 0

for passport in passports:
    cid = False
    if "cid" in passport:
        cid = True
    amount = len(passport.keys())
    if amount == 8 or (cid == False and amount == 7):
        validPassports += 1

print(validPassports)



        