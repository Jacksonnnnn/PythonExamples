side1 = int(raw_input("In inches, what is the length of side 1?  "))
side2 = int(raw_input("In inches, what is the length of side 2?  "))
side3= int(raw_input("In inches, what is the length of side 3?  "))

if side1 == side2 and side2 == side3:
	print "Your triangle is an equilateral triangle."
if side1 == side2 and side1 != side3 or side2 == side3 and side2 != side1:
	print "Your triangle is an isosceles triangle."
if side1 != side2 and side1 != side3 or side2 != side3 and side2 != side1:
	print "Your triangle is a scalene."