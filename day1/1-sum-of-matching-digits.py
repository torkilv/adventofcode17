import sys

digits = sys.argv[1]

matching_digit_sum = 0
for i in xrange(len(digits)-1):
	if digits[i] == digits[i+1]:
		matching_digit_sum += int(digits[i])
if digits[0] == digits[-1]:
	matching_digit_sum += int(digits[0])

print matching_digit_sum
