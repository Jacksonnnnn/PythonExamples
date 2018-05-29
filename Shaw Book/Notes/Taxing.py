#Asking what the subtotal amount is
subtotal = raw_input("What is your subtotal amount?  ")

#The tax is 6%
tax = 1.06%

#The Total equals the subttotal times the tax
total = subtotal * tax

#Printing the total to the user
print "Your with the subtotal of $%s and the tax at 6%, your total is $%s." % (subtotal, total)