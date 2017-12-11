from collections import Counter, defaultdict

moves = open("11-input", "r").read().strip().split(",")

frequencies = defaultdict(lambda: 0, Counter(moves))
print frequencies

for i in range(frequencies["ne"]):
	if frequencies["nw"] > 0:
		frequencies["n"] += 1
		frequencies["nw"] -= 1
		frequencies["ne"] -= 1
	elif frequencies["sw"] > 0:
		frequencies["ne"] -= 1
		frequencies["sw"] -= 1
	else:
		break

for i in range(frequencies["se"]):
	if frequencies["sw"] > 0:
		frequencies["s"] += 1
		frequencies["sw"] -= 1
		frequencies["se"] -= 1

	elif frequencies["nw"] > 0:
		frequencies["nw"] -= 1
		frequencies["se"] -= 1
	else:
		break

for i in range(frequencies["n"]):
	if frequencies["s"] > 0:
		frequencies["s"] -= 1
		frequencies["n"] -= 1
	elif frequencies["se"] > 0:
		frequencies["ne"] += 1
		frequencies["n"] -= 1
		frequencies["se"] -= 1
	elif frequencies["sw"] > 0:
		frequencies["nw"] += 1
		frequencies["n"] -= 1
		frequencies["sw"] -= 1
	else:
		break
for i in range(frequencies["s"]):
	if frequencies["ne"] > 0:
		frequencies["se"] += 1
		frequencies["s"] -= 1
		frequencies["ne"] -= 1
	elif frequencies["nw"] >0:
		frequencies["sw"] += 1
		frequencies["s"] -= 1
		frequencies["nw"] -= 1

	else:
		break


print frequencies
print sum(frequencies.values())



