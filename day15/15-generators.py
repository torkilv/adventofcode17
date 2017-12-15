
class Generator:

	def __init__(self, start, multiplicator, divisor):
		self.current = start
		self.multiplicator = multiplicator
		self.divisor = divisor


	def next(self):
		self.current = (self.current * self.multiplicator) % 2147483647 
		while self.current % self.divisor != 0:
			self.current = (self.current * self.multiplicator) % 2147483647 

		return self.current


def compare_lowest_16(a,b):
	return str(bin(a))[-16:] == str(bin(b))[-16:]


generatorA = Generator(516, 16807, 4)
generatorB = Generator(190, 48271, 8)

#generatorA = Generator(65, 16807, 1)
#generatorB = Generator(8921, 48271,1)



count = 0
for i in xrange(5*10**6):
	count += compare_lowest_16(generatorA.next(), generatorB.next())

print count


