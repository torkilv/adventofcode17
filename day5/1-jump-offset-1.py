

instructions = [int(line.strip()) for line in open("input", "r")]

current_step = 0
current_instruction = 0
steps = 0
while current_step > -1 and current_step < len(instructions):
	steps += 1
	current_instruction = instructions[current_step]
	instructions[current_step] += 1

	current_step += current_instruction


print steps
 

