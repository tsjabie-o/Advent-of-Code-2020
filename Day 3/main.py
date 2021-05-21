data = list()
with open("./Day 3/data.txt", "r") as input:
    for line in input:
        data.append(line)


def CountTrees(y_change, x_change):
    x_pos = 0
    y_pos = 0
    trees = 0
    while y_pos < len(data):
        if x_pos >= len(data[y_pos]) - 1:
            x_pos = x_pos % (len(data[y_pos]) - 1)
        
        if data[y_pos][x_pos] == '#':
            trees += 1
        x_pos += x_change
        y_pos += y_change
    return trees

print(
    CountTrees(1, 3) * 
    CountTrees(1,1) * 
    CountTrees(1, 5) * 
    CountTrees(1, 7) * 
    CountTrees(2, 1)
    )