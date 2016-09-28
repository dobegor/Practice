from random import uniform
import sys

if len(sys.argv) > 1:
	n = int(sys.argv[1])

	sum = 0
	for i in range(0, n):
		rand = uniform(-1, 1)
		print("%.4f" % rand)
		sum += rand
	
	print("Average value is %.4f" % (sum / n))
else: 
	print("Please specify quanitity of random numbers")
