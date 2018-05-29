hyears = int(raw_input("How many human years would you like to convert?  "))

if hyears <= 2:
	dyears = hyears * 10.5
	print "%s human years equates to %s dog years." % (hyears, dyears)
elif hyears < 0:
	print "%s is not an acceptable answer. Answer must be postitive!" % hyears
else:
	dyears1 = 2 * 10.5
	dyears2 = (hyears - 2) * 4
	tdyears = dyears1 + dyears2
	print "%s human years equates to %s dog years." % (hyears, tdyears)