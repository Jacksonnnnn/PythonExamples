kilo = float(raw_input("How many kilometers have you traveled?  "))

def cabfare(a):
	distance = (a / 225.308) * 0.25
	fare = 4 + distance
	print "Your total cab fare is %s for %s kilometers traveled" % (fare, a)

cabfare(kilo)