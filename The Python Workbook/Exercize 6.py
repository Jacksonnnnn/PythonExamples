cost = float(raw_input("How much was your meal?  "))
tax = cost * 0.06
tip = cost * 0.18
 
total = cost + tax + tip
 
print "The grandtotal of your meal is: $%s." % total