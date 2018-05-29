from math import *
a = float(raw_input("What is the numerical value of a?  "))
b = float(raw_input("What is the numerical value of b?  "))
c = float(raw_input("What is the numerical value of c?  "))
d = (b ** 2) * 4*(a)*(c)
if d < 0:
	print "There are no real roots to your equation."
elif d == 0:
	root1 = ((b - 0) + sqrt(d))/ 2*(a)
	root2 = ((b - 0) - sqrt(d))/ 2*(a)
	print "There is one real root to your equation. %s and %s." % (root1, root2)
elif d > 0:
	root1 = ((b - 0) + sqrt(d))/ 2*(a)
	root2 = ((b - 0) - sqrt(d))/ 2*(a)
	print "There is two real roots to your equation. %s and %s." % (root1, root2)