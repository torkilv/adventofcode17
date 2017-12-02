
import itertools, operator

spreadsheetFile = open("input-2", "r")


checkSum = 0
for line in spreadsheetFile:
	numbers = map(int, line.split())

	combinations = itertools.permutations(numbers, 2)
	for combination in combinations:
		if combination[0] % combination[1] == 0:
			checkSum += combination[0] / combination[1]
			break


print checkSum

