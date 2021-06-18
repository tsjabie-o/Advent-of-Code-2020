import math

bpasses = list()
with open("./Day 5/data.txt") as data:
    for line in data:
        bpasses.append(line)

def BSP_Search(bpass, max_, trig):
    min_ = 0
    for i in range(len(bpass)):
        if bpass[i] == trig:
            max_ = min_ + math.floor((max_ - min_)/2)
        else:
            min_ += math.ceil((max_ - min_)/2)
    return max_

def CalcSeatID(row, column):
    return row * 8 + column

seats = dict()

for bpass in bpasses:
    row = BSP_Search(bpass[0:7], 127, "F")
    col = BSP_Search(bpass[7:10], 7, "L")
    seatID = CalcSeatID(row, col)
    seats[seatID] = (row, col)

#* Part 1
maxSeatID = max(seats)
print(f"Highest SeatID: {maxSeatID}")


#* Part 2
for i in range(1024):
    if i not in seats:
        if i - 1 in seats and i + 1 in seats:
            mySeat = i
print(f"My seat: {mySeat}")