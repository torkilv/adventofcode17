


def removeGarbage(string):

	keep = True
	cleanString = ""
	ignore = False
	garbageCount = 0
	for i in xrange(len(string)):

		if ignore:
			ignore = False
			continue
		
		letter = string[i]

		if string[i] == "!":
			ignore = True
			continue

		if keep and string[i] == "<":
			keep = False
			continue


		if not keep and letter == ">":
			keep = True
			continue

		if keep and letter in "{}":
			cleanString += letter
		elif not keep:
			garbageCount += 1
		

	return cleanString, garbageCount



string = open("9-input", "r").read()


string, garbageCount = removeGarbage(string)

value = 0
score = 0
for letter in string:
	if letter == "{":
		value += 1
	elif letter == "}":
		score += value
		value -= 1
		value = max(0, value)

print score, garbageCount







