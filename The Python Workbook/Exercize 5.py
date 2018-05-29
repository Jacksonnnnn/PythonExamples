less = int(raw_input("How many bottles are one liter or less?  "))
more = int(raw_input("How many bottles are more than one liter?  "))

oneliter = less * 0.10
morethanoneliter = more * 0.25

total = oneliter + morethanoneliter

print "You will recieve $%s" % total