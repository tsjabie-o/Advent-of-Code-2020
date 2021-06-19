
from typing import MutableMapping


def ParseInput():
    with open("./Day 6/data.txt") as data:
        rawdata = data.read()
    groups = rawdata.split("\n\n")
    groups = [group.replace("\n", " ") for group in groups]
    return groups

def CountQuestions1(group):
    questions = list()
    for char in group:
        if char not in questions and char != " ": questions.append(char)
    return questions

def CountQuestions2(group):
    passengers = group.split()
    mutual = [char for char in passengers[0]]
    for char in passengers[0]:
        for i in range(1, len(passengers)):
            if char not in passengers[i]:
                mutual.remove(char)
                break
    return mutual

groups = ParseInput()

# Part one
total1 = 0
for group in groups:
    questions = CountQuestions1(group)
    total1 += len(questions)

# Part two
total2 = 0
for group in groups:
    # print(group)
    questions = CountQuestions2(group)
    # print(questions)
    total2 += len(questions)
