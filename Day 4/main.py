import re
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

print("Valid passports, part 1: {}".format(len(validPassports)))

validPassports2 = list()

for passport in validPassports:
    if not (
        # Years
        int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002
        and int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020
        and int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030
    ):
        continue

    # Regular expressions checks
    
    # Height
    unit = passport["hgt"][-2:]
    if unit == "cm":
        height = int(passport["hgt"][:-2])
        if not (height >= 150 and height <= 193):
                    continue
    elif unit == "in":
        height = int(passport["hgt"][:-2])
        if not (height >= 59 and height <= 76):
            continue
    else:
        continue
    
    # Hair colour
    if not re.search(r"#[a-f0-9]{6}", passport["hcl"]):
        continue

    # Eye colour
    if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue

    # Passport ID
    if not re.search(r"^[0-9]{9}$", passport["pid"]):
        continue

    validPassports2.append(passport)

print("Valid passports, part 1: {}".format(len(validPassports2)))