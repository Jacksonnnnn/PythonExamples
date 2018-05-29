moneyin = float(raw_input("You'll be buying a Salad and a Medium Drink today. The total will be $5.00. How much are you putting in?  "))
change = 5.00 - moneyin
changeneg = abs(change)

if change <= 0:
	print "Thank you! You're change is $%s. Have a great day." % changeneg
	
if change > 0:
	print "Hey! You still owe some money! $%s" % change
	moneytwo = float(raw_input("Please put in the right of the amount of money you owe.  "))
	
	if moneytwo <= 0:
		print "Thank you for shopping! Your change is $%s." % changeneg
	
	if moneytwo > 0:
		print "Get out please before our bouncers make you bounce please."