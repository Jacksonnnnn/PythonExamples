from math import *

length1 = int(raw_input("What is the length of one side of your triangle?  "))
length2 = int(raw_input("What is the length of the other side of your triangle?  "))

def pythagoreantherum(side1, side2):
	a = side1 ** 2
	b = side2 ** 2
	c = a + b
	hypot = sqrt(c)
	print "Your sides are %s and %s, which gives the hypotenuse as %s" % (length1, length2, hypot)
	
pythagoreantherum(length1, length2)