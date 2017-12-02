
import itertools

spreadsheetFile = open("input-2", "r");


checkSum = 0;
for line in spreadsheetFile:
	numbers = map(int, line.split())
	combinations = itertools.product(numbers);
	modulos = map(lambda x: apply(%, x), itertools.product(numbers))
	checksum += apply(/, combinations[modulos.where(0)]);


print checkSum

