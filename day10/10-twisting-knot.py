

sequence = range(256)

current_position = 0
skip_size = 0
lengths = map(lambda s: int(s.strip()), open("10-input", "r").read().strip().split(","))

print lengths
for length in lengths:
	start = current_position
	if current_position + length >= len(sequence):
		extra = (current_position + length) % len(sequence)

		list_to_reverse = sequence[start:]
		list_to_reverse.extend(sequence[:extra])

		reverse = list(reversed(list_to_reverse))

		sequence[start:] = reverse[:256-start]
		sequence[:extra] = reverse[256-start:]

	else:
		end = current_position + length 
		sequence[start:end] = list(reversed(sequence[start:end]))



	current_position = (current_position + length + skip_size) % len(sequence) 
	skip_size += 1

print sequence[0]*sequence[1]