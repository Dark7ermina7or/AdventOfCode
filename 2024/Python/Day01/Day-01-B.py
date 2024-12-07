PuzzleInput = open("Day-01-input.txt", "r").read().splitlines()

ListA = []
ListB = []
ListCount = []

output = 0

for x in PuzzleInput:
    tmp = x.split()
    ListA.append(int(tmp[0]))
    ListB.append(int(tmp[1]))

for x in ListA:
    ListCount.append(0)
    for y in ListB:
        if x == y:
            ListCount[-1] += 1

for idx, x in enumerate(ListCount):
    output += ListA[idx] * ListCount[idx]

print(output)