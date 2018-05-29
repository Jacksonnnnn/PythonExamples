amount_deposited = int(raw_input("How much money have you deposited into your account?  "))

interest = 1.04

year1 = amount_deposited * interest
year2 = 2 * (amount_deposited * interest)
year3 = 3 * (amount_deposited * interest)

print "After 1 year, your account will be this much: $%s." % year1
print "After 2 year, your account will be this much: $%s." % year2
print "After 3 year, your account will be this much: $%s." % year3