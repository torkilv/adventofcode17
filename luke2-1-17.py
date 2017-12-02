
spreadsheetFile = open("input-2", "r");

checkSum = 0;
for line in spreadsheetFile:
	numbers = map(int, line.split())
	difference = max(numbers) -  min(numbers);
	checkSum += difference


print checkSum

