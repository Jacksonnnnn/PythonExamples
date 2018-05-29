bread_price = 3.49
discount = 0.60

loaf_number = int(raw_input("Number of day old loaves?  "))
reg_price = loaf_number * bread_price
discounted = reg_price * discount
total = reg_price - discounted

print "Regular Price: %5.2f" % reg_price
print "Discount:     -%5.2f" % discounted
print "Total:         %5.2f" % total