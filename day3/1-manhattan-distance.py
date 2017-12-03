import sys


original_square  = int(sys.argv[1])
n = 1
passes = 0

while original_square > n**2:
	n += 2
	passes += 1


steps_left_on_last_cycle = original_square - n**2
spot_on_side = steps_left_on_last_cycle % (n-1)
mid_point = n/2
perpendicular_steps = abs(spot_on_side - mid_point)

print passes + perpendicular_steps


