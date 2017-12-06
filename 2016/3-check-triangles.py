import sys

valid_triangles = 0

triangles = []

if len(sys.argv) > 1:
	i = 0
	temp_triangles = [[],[],[]]
	for line in open("3-input", "r"):
		j = 0
		for s in line.split():
			temp_triangles[j].append(int(s.strip()));
			j += 1
		i += 1

		if i == 3:
			triangles.extend(temp_triangles)
			temp_triangles = [[],[],[]]
			i = 0

else:

	for line in open("3-input", "r"):
		triangles.append(map(lambda s : int(s.strip()), line.split()))


for triangle in triangles:
	max_length = max(triangle)
	triangle.remove(max_length)
	valid_triangles += sum(triangle) > max_length

print valid_triangles

