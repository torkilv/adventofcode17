
import sys

keypads = [
[[1,4,7],[2,5,8],[3,6,9]],
[[False, False,5], [False, 2,6,"A"], [1,3,7, "B", "D"], [False, 4,8, "C"], [False, False, 9]]]


keypad = keypads[0]
cur_pos = [1,1]
column_borders = [0,2]*3
if len(sys.argv) > 1:
	keypad = keypads[1]
	cur_pos = [0,2]
	column_borders = [[2,2],[1,3],[0,4],[1,3],[2,2]]


moves = {
	"U": [0,-1],
	"D": [0, 1],
	"L": [-1,0],
	"R": [1,0]
}



for line in open("2-input","r"):
	for order in line.strip():
		move = moves[order.strip()]

		if move[0] != 0:
			new_pos = min(len(keypad)-1,max(0, cur_pos[0]+ move[0]))

			if cur_pos[1] < len(keypad[new_pos]) and keypad[new_pos][cur_pos[1]]:
				cur_pos[0] = new_pos
		else:
			cur_pos[1] = min(column_borders[cur_pos[0]][1], 
				max(column_borders[cur_pos[0]][0], cur_pos[1] + move[1]))


	print keypad[cur_pos[0]][cur_pos[1]]