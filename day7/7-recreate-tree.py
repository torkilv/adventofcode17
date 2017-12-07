

class Node:
	def __init__(self, value, name):
		self.value = value;
		self.name = name;
		self.parent = False;
		self.children = []

	def addParent(self, branch):
		self.parent = branch;

	def addChild(self, branch):
		self.children.append(branch)

	def getValue(self):
		value = self.value
		if len(self.children) > 0:
			for child in self.children:
				value += child.getValue()
		return value

	def is_unbalanced(self, needed_value):
		
		children = self.children
		if len(self.children) > 0:
			values = [child.getValue() for child in self.children]

			if len(set(values)) == 1:
				return needed_value - (self.getValue() - self.value)
			if len(children) == 1:
				return children[0].is_unbalanced(children[1].getValue())

			unique_item = 0
			not_unique = 1
			while values.count(values[unique_item]) > 1:
				not_unique = 0
				unique_item += 1

			return children[unique_item].is_unbalanced(children[not_unique].getValue())


		else:
			return needed_value - (self.getValue() - self.value)



node_dict = {}
for line in open("7-input", "r"):
	name = line.split("(")[0][:-1]
	value = int(line.split("(")[1].split(")")[0])
	neighbors = []
	if ">" in line:	
		neighbors = map(lambda s: s.strip(), line.split(">")[1].split(","))

	newNode = False
	if not node_dict.get(name):
		newNode = Node(value, name)
		node_dict[name] = newNode
	else:
		newNode = node_dict[name]
		newNode.value = value
		newNode.name = name
	
	if len(neighbors) > 0:
		for neighbor in neighbors:
			
			if not node_dict.get(neighbor, False):
				neighborNode = Node(0, neighbor)
				node_dict[neighbor] = neighborNode
			else:
				neighborNode = node_dict[neighbor]
			neighborNode.addParent(newNode)
			newNode.addChild(neighborNode)


while newNode.parent:
	newNode = newNode.parent



print newNode.name

print newNode.is_unbalanced(0)