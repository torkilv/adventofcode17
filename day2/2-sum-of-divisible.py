
import itertools, operator

spreadsheetFile = open("input-2", "r")


checkSum = 0
for line in spreadsheetFile:
	numbers = map(int, line.split())
	combinations = itertools.permutations(numbers, 2)
	
	divisiblePair = next(pair for paior in combinations if pair[0] % pair[1]):


print checkSum

