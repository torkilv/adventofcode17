from collections import defaultdict

counter = 0

inputString = open("13-input","r")

layerDepths = defaultdict(lambda: 0)
for line in inputString:
	layerNumber, layerDepth = map(lambda s: s.strip(), line.split(": "))
	layerDepths[int(layerNumber)] = int(layerDepth)


severity = 0
layers = max(layerDepths.keys())+1
layerPos = [-2]*layers
scan_directions = [1]*layers

for j in xrange(len(layerPos)):
	if j in layerDepths:
		layerPos[j] = 0
	else:
		scan_directions[j] = 0

for i in xrange(layers):
	print "picosecond ", counter, "layers", layerPos
	if layerPos[i] == 0:
		print "hit layer ", i, "with depth", layerDepths[i]

		severity += i * layerDepths[i]

	counter += 1
	for j in xrange(len(layerPos)):
		if layerPos[j] == layerDepths[j]-1:
			scan_directions[j] = -1
		elif layerPos[j] == 0:
			scan_directions[j] = 1
		
		layerPos[j] += scan_directions[j]

print severity



