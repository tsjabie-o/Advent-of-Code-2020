data = list()
with open("./Day 3/data.txt", "r") as input:
    for line in input:
        data.append(line)

x_pos = 0
y_pos = 0
trees = 0
while y_pos < len(data):
    if x_pos >= len(data[y_pos]) - 1:
        x_pos = x_pos % (len(data[y_pos]) - 1)
    
    if data[y_pos][x_pos] == '#':
        trees += 1
    x_pos += 3
    y_pos += 1

print(trees)