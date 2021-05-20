data = []

with open(".\Day 1\data.txt", "r") as input:
    for x in input:
        data.append(int(x))

for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i] + data[j] == 2020:
            print(data[i] * data[j])