print sum([len(set(map(lambda x: "".join(sorted(x)),phrase.split()))) == len(phrase.split()) 
	for phrase in open('input', 'r')])
