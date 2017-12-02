
import itertools

spreadsheetFile = open("input-2", "r")


checkSum = 0
for line in spreadsheetFile:
	numbers = map(int, line.split())
	combinations = list(itertools.permutations(numbers, 2))
	modulos = map(lambda pair: (pair[0] % pair[1]), combinations)

	divisiblePair = combinations[modulos.index(0)]
	checkSum += divisiblePair[0] / divisiblePair[1]


print checkSum

