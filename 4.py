import math
import sys

def ln(number):
	return math.log(number)

def ValidNumber(a):
	if a > 0 : 
		return True
	else:
		return False # not really, just assuming we're Real.

def DisplayResult(a, b):
	print("ln(%s) = %.6f" % (a, b))

def PrintError(a):
	print("ln(%s) is illegal" % a)

def Process(a):
	arg = float(a)
	if ValidNumber(arg):
		DisplayResult(arg, ln(arg))
	else:
		PrintError(arg)


def First():
	for r in sys.argv[1:]:
		Process(r)

def Second():
	for i in range(1, len(sys.argv)):
		Process(sys.argv[i])

def Third():
	i = 1
	while i < len(sys.argv):
		Process(sys.argv[i])
		i += 1

def Fourth():
	i = 1
	while 1:
		try:
			Process(sys.argv[i])
			i += 1
		except:
			break

First()
Second()
Third()
Fourth()
