
spreadsheetFile = open("input-2", "r");

checkSum = 0;
for line in spreadsheetFile:
	numbers = map(int, line.split())
	for i in xrange(len(numbers)):
		for j in xrange(len(numbers)):
			if i==j:
				continue

			if numbers[i] % numbers[j] == 0:
				checkSum += numbers[i]/numbers[j]


print checkSum

