

sequence = range(256)

current_position = 0
skip_size = 0
lengths = [ord(s) for s in open("10-input", "r").read().strip()]

salt = [17,31,73,47,23]
lengths.extend(salt)
lengths = lengths * 64
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

hex_values = []
for x in range(16):
	hex_values.append(reduce(lambda x,y:x^y, sequence[x*16:(x+1)*16]))

hex_string = ""

for hex_value in hex_values:
	s = "%0x" % hex_value
	if len(s) == 1:
		s = "0"+s
	hex_string += s

print hex_string