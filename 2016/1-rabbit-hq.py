



orders = open("1-input", "r").read().split(",")

orders = map(lambda s: s.strip(), orders)
axis = 1
heading = 1

coordinates = [0,0]

visited_spots = {}
visited_spots[str(coordinates)] = True
visited_twice_found = False
for order in orders:
	axis = int(not axis)
	if order[0] == "R" and axis == 1:
		heading = heading * -1
	elif order[0] == "L" and axis == 0:
		heading = heading * -1

	for i in xrange(int(order[1:])):

		coordinates[axis] += heading 
		if not visited_twice_found and visited_spots.get(str(coordinates)):
			print "Already visited", sum(map(abs, coordinates)), coordinates
			visited_twice_found = True

		else:
			visited_spots[str(coordinates)] = True


print sum(map(abs, coordinates))
