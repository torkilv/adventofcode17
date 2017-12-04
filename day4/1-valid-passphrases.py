print sum([len(set(phrase.split())) == len(phrase.split()) 
	for phrase in open('input', 'r')])
