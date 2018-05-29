num = int(raw_input("What is the number you've chosen (1-12)?  "))
def ordinal():
	if num == 1:
		ordinal = "first"
		print "Your number, %s, has the ordinal unit of %s." % (num, ordinal)
	elif num == 2:
		ordinal = "second"
		print "Your number, %s, has the ordinal unit of %s." % (num, ordinal)
	elif num == 3:
		ordinal = "third"
		print "Your number, %s, has the ordinal unit of %s." % (num, ordinal)
	elif num == 4:
		ordinal = "fourth"
		print "Your number, %s, has the ordinal unit of %s." % (num, ordinal)
	elif num == 5:
		ordinal = "fifth"
		print "Your number, %s, has the ordinal unit of %s." % (num, ordinal)
	elif num == 6:
		ordinal = "sixth"
		print "Your number, %s, has the ordinal unit of %s." % (num, ordinal)
	elif num == 7:
		ordinal = "seventh"
		print "Your number, %s, has the ordinal unit of %s." % (num, ordinal)
	elif num == 8:
		ordinal = "eighth"
		print "Your number, %s, has the ordinal unit of %s." % (num, ordinal)
	elif num == 9:
		ordinal = "ninth"
		print "Your number, %s, has the ordinal unit of %s." % (num, ordinal)
	elif num == 10:
		ordinal = "tenth"
		print "Your number, %s, has the ordinal unit of %s." % (num, ordinal)
	elif num == 11:
		ordinal = "eleventh"
		print "Your number, %s, has the ordinal unit of %s." % (num, ordinal)
	elif num == 12:
		ordinal = "twelfth"
		print "Your number, %s, has the ordinal unit of %s." % (num, ordinal)
	else:
		print "THERE IS A REASON I SAID 1-12. YOU MUST REALIZE YOUR ACTIONS HAVE CONSEQUENCES!"
ordinal()