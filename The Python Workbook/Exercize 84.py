def median(a, b, c):
	if a < b and b < c or a > b and b > c:
		return b
	if b < a and a < c or b > a and a > c:
		return a
	if c < a and b < c or c > a and b > c:
		return c

def alternateMedian (a, b ,c):
	return (a + b + c) - min(a, b, c) - max (a, b, c)

def main():
	x = float(raw_input("What is the first value?  "))
	y = float(raw_input("What is the second value?  "))
	z = float(raw_input("What is the third value?  "))
	print "The median value is: ", median(x, y, z)
	print "The median using the alternate method is: ", alternateMedian(x, y, z)
	
main()