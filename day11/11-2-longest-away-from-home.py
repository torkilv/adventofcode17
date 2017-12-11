moves = open("11-input", "r").read().strip().split(",")

max_distance_away = 0
cur_position = [0,0]

directions = {
	"ne": [1,1],
	"n": [0,2],
	"nw": [-1, 1],
	"sw": [-1, -1],
	"s": [0, -2],
	"se": [1,-1]
}

def calculate_distance_home(pos):
	distance = 0
	pos = map(abs, pos)
	while pos[0] != 0:
		pos = [pos[0]-1, pos[1]-1]
		distance +=1
	
	distance += pos[1]/2

	return distance




for move in moves:
	direction = directions[move]
	cur_position = [cur_position[0]+direction[0], cur_position[1]+direction[1]]
	cur_dist = calculate_distance_home(cur_position)
	if cur_dist > max_distance_away:
		max_distance_away = cur_dist

print max_distance_away
print cur_dist

