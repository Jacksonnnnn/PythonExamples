numitems = int(raw_input("How many items are being shipped?  "))

def shippingcalc():
	if numitems == 1:
		price = 10.95
	elif numitems >= 2:
		price = ((numitems - 1) * 2.95) + 10.95
	
	print "Your total shipping cost of %s items will be $%s." % (numitems, price)
shippingcalc()