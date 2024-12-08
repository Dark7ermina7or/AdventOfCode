PuzzleInput = open("Day-02-input.txt", "r").read().splitlines()

safeCount = 0

for line in PuzzleInput:
    currLine = list(map(int, line.split()))

    if len(currLine) == 1:
        safeCount += 1
        continue

    if all(currLine[i] > currLine[i + 1] for i in range(len(currLine) - 1)) or all(currLine[i] < currLine[i + 1] for i in range(len(currLine) - 1)):
        if all(1 <= abs(currLine[i + 1] - currLine[i]) <= 3 for i in range(len(currLine) - 1)):
            safeCount += 1

print(safeCount)

