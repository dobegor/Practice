import random
import sys

# number of experiments
n = int(sys.argv[1])
cnt = 0
for i in range(0, n):
	for f in range(0, 2):
                # this isn't really random, but nobody cares
		r = random.randint(1, 6)
		#print("%i experiment = %i" % (i, r))
		if(r == 6):
                        # why the hell there's no increment?
			cnt +=1
                        # we only need first 6, sorry bro
			break
p = cnt / n
print("Probability = %.3f" % p)

# The probability is 11/36 == 0.305(5)
# Ten thousands of operations tend to be enough.
