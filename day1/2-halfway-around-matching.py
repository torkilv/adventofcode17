import sys

digits = sys.argv[1]

matching_digit_sum = 0
for i in xrange(len(digits)):
	halfwayaround = (i + len(digits)/2) %  len(digits)
	if digits[i] == digits[halfwayaround]:
		matching_digit_sum += int(digits[i])


print matching_digit_sum
