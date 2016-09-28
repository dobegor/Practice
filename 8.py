import random
import sys

# number of experiments
n = int(sys.argv[1])
cnt = 0
for i in range(0, n):
	sum = 0
	for f in range(0, 4):
		r = random.randint(1, 6)	
		sum += r		
	
	if(sum < 9):
		cnt += 1		

p = cnt / n
print("Probability of profit is %.4f" % p)
print("Keep in mind that gamble games are prohibited.")

