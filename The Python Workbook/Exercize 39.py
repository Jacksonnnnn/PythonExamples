level = int(raw_input("Enter the amount of decibles...  "))

if level == 130:
	print "Your noise is equivelent to that of a Jackhammer."
elif level == 106:
	print "Your noise is equivelent to that of a Gas lawnmower."
elif level == 70:
	print "Your noise is equivelent to that of an Alarm Clock."
elif level == 40:
	print "Your noise is equivelent to that of a Quiet Room."
elif level > 130:
	print "Your noise is greater than that of a Jackhammer."
elif level < 130 or level > 106:
	print "Your noise is louder than a Gas Lawnmower, but quieter than a Jackhammer."
elif level < 106 or level > 70:
	print "Your noise is louder than an Alarm Clock, but quieter than a Gas lawnmower."
elif level < 70 or level >  40:
	print "Your noise is louder than a Quiet Room, but is quieter than an Alarm Clock."
elif level < 40:
	print "Your noise is quieter than a Quiet Room."