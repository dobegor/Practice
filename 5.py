import sys
import math

try:	
	outfilename = sys.argv [1]
except:
	print("Usage:", sys.argv[0], "outfile values...")
	sys.exit (1)

ofile = open(outfilename , "w")

def  myfunc(y):
	if y  >= 0.0:
		return y**5* math.exp(-y)		
	else:
		return  0.0

# every arg with index starting with 2 is a left number to process
# therefore, index+1 is a right number to apply function on
for i in range(2, len(sys.argv) - 1, 2):
	x = float(sys.argv[i])
	y = float(sys.argv[i + 1])
	fy = myfunc(y)
	ofile.write("(%g, %g)\n" % (x,fy))	
ofile.close()

