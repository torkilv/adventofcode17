


memory_blocks = map(int, open("input", "r").read().split())


memory_string = ",".join(map(str,memory_blocks))

visited_structure = {} 

redistributions = 0
while not visited_structure.get(memory_string):

	
	visited_structure[memory_string] = redistributions
	redistributions += 1


	max_block = max(memory_blocks)
	current_index = memory_blocks.index(max_block)
	memory_blocks[current_index] = 0

	while max_block > 0:
		current_index += 1
		current_index = current_index % len(memory_blocks)

		max_block -= 1
		memory_blocks[current_index] += 1

	memory_string = ",".join(map(str,memory_blocks))

print redistributions
print redistributions -  visited_structure[memory_string] 

