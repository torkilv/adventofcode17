from collections import defaultdict

counter = 0

inputString = open("13-input","r")

layerDepths = defaultdict(lambda: 0)
for line in inputString:
	layerNumber, layerDepth = map(lambda s: s.strip(), line.split(": "))
	layerDepths[int(layerNumber)] = int(layerDepth)

layers = max(layerDepths.keys())+1


max_layer_reached = 0

def scanFromSecond(startSecond):
	layerPos = [-2]*layers
	scan_directions = [1]*layers
	cur_pos = 0
	global max_layer_reached

	for j in xrange(len(layerPos)):
		if j in layerDepths and layerDepths[j] != 0:
			
			mod = startSecond % max(1, ((2*layerDepths[j])-2))

		
			if mod > (layerDepths[j] - 1):
				scan_directions[j] = -1
				layerPos[j] =  2 * layerDepths[j] - 2  - mod 
			else:
				layerPos[j] = mod 
		else:
			scan_directions[j] = 0


	for i in xrange(layers):
		#print "StartSecond", startSecond, "picosecond ", cur_pos, "layers", layerPos
		if cur_pos >= 0 and layerPos[cur_pos] == 0:
			#print "hit!"
			if cur_pos > max_layer_reached:
				print "New max layer", cur_pos
				max_layer_reached = cur_pos
			return False

		cur_pos += 1
		for j in xrange(len(layerPos)):
			if layerPos[j] == layerDepths[j]-1:
				scan_directions[j] = -1
			elif layerPos[j] == 0:
				scan_directions[j] = 1
		
			layerPos[j] += scan_directions[j]
	return True



while not scanFromSecond(counter):
	
	counter += 1
print counter



