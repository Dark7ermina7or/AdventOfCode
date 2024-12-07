PuzzleInput = open("Day-01-input.txt", "r").read().splitlines()

ListA = []
ListB = []
ListDist = []

output = 0

for x in PuzzleInput:
    tmp = x.split()
    ListA.append(int(tmp[0]))
    ListB.append(int(tmp[1]))

while len(ListA) > 0:
    ListDist.append(int(ListA.pop(ListA.index(min(ListA))))-int(ListB.pop(ListB.index(min(ListB)))))

    if ListDist[-1] < 0:
        ListDist[-1] = ListDist[-1]*(-1)

for x in ListDist:
    output += x

print(output)