from collections import defaultdict
import sys

def turn_left(x,y):
	if x == 1:
		return 0, 1
	elif y == 1:
		return -1, 0
	elif x == -1:
		return 0, -1
	elif y == -1:
		return 1,0

def sum_of_neighbors(pos, positions):
	sum_of_neighbors = 0

	for neighbor in [[0,1],[1,1],[1,0], [1,-1],[0,-1], [-1,-1], [-1,0], [-1,1]]:
		neighbor_pos = map(lambda x: x[0]+x[1], zip(pos, neighbor))
		sum_of_neighbors += positions[str(neighbor_pos)]
	return sum_of_neighbors

x_dir = 0
y_dir = -1

positions = defaultdict(lambda: 0)

step = 0
side_length = 0

side_lengths = -1
cur_pos = [0,0]
value = 1

max_value = int(sys.argv[1])

positions[str(cur_pos)] = value

while value <= max_value:
	if step == side_length:
		step = 0
		x_dir, y_dir = turn_left(x_dir, y_dir)

		if side_lengths == 1:
			side_length += 1
			side_lengths = 0
		else:
			side_lengths += 1
	else:
		step += 1

	cur_pos = [cur_pos[0]+x_dir, cur_pos[1]+y_dir]
	value = sum_of_neighbors(cur_pos, positions)
	positions[str(cur_pos)] = value

print value



