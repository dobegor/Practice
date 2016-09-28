import sys
import math

try:
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
except:
    print("Usage:", sys.argv[0], "infile  outfile")
    sys.exit(1)

ifile = open(infilename, "r")
ofile = open(outfilename, "w")

# iterate over lines in file
for line in ifile:
    substr = line.split()
    sum = 0
    # calculate average value
    for number in substr:
        val = float(number)
        sum += val
        ofile.write("%12.6f" % val)
    ofile.write("%12.6f\n" % (sum / len(substr)))
    
# close file handlers
ifile.close()
ofile.close()
