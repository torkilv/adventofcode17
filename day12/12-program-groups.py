from collections import defaultdict
import sys



class Program:
	 visited = False;

	 def __init__(self, name):
	 	self.name = name
	 	self.neighbors = set([])

	 def addNeighbor(self, program):
	 	self.neighbors.add(program)

	 def addNeighbors(self,names):
	 	for name in names:
	 		if not programs[name]:
	 			programs[name] = Program(name)
	 		self.neighbors.add(name)
	 		programs[name].addNeighbor(self.name)

	 def findGroupSize(self):
	 	if self.visited:
	 		return 0;
	 	else:
	 		self.visited = True;
	 		groupSize = 1
	 		for neighbor in self.neighbors:
	 			groupSize += programs[neighbor].findGroupSize()

	 		return groupSize

programs = defaultdict(lambda: False)
lines = open("12-input", "r")

for line in lines:
	name, neighborString = line.split("<->")
	name = name.strip()
	neighbors = map(lambda s: s.strip(), neighborString.split(","))


	if not programs[name]:
		programs[name] = Program(name)

	programs[name].addNeighbors(neighbors)

groups = 1
zero_group_size = programs["0"].findGroupSize()

for program in programs:
	if not programs[program].visited:
		programs[program].findGroupSize()
		groups += 1

print zero_group_size, groups
