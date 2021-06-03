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

validPassports = list()

for passport in passports:
    cid = False
    if "cid" in passport:
        cid = True
    amount = len(passport.keys())
    if amount == 8 or (cid == False and amount == 7):
        validPassports.append(passport)

print(len(validPassports))

validPassports2 = list()

for passport in validPassports:
    if (
        int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002
        and int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020
        and int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030



        and passport["hgt"][-2:] == "cm" or passport["hgt"][-2:] == "in"



        and int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020
        and int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020
        and int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020
        and int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020
    )
