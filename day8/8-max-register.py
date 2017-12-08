
from collections import defaultdict

registers = defaultdict(lambda: 0)

orders = {
	"dec": -1,
	"inc": 1
}

maxValueEver = 0

for instructionLine in open("8-input", "r"):
	instruction = map(lambda s: s. strip(), instructionLine.split())
	register = instruction[0]
	order = orders[instruction[1]]

	predicateValue = registers[instruction[4]]
	predicate = str(predicateValue)+" ".join(instruction[5:])

	if eval(predicate):
		registers[register] += order * int(instruction[2])
		if registers[register] > maxValueEver:
			maxValueEver = registers[register]

print registers[max(registers, key=registers.get)]
print maxValueEver






