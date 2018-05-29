gradep = float(raw_input("What is your grade point for a class?  "))

if gradep <= "1.0":
	print "Your grade is a D."
elif gradep <= "1.3" and gradep > "1.0":
	print "Your grade is a D+."
elif gradep <= "1.7" and gradep > "1.3":
	print "Your grade is a C-."
elif gradep <= "2.0" and gradep > "1.7":
	print "Your grade is a C."
elif gradep <= "2.3" and gradep > "2.0":
	print "Your grade is a C+"
elif gradep <= "2.7" and gradep > "2.3":
	print "Your grade is a B-."
elif gradep <= "3.0" and gradep > "2.7":
	print "Your grade is a B."
elif gradep <= "3.3" and gradep > "3.0":
	print "Your grade is a B+."
elif gradep <= "3.7" and gradep > "3.3":
	print "Your grade is an A-."
elif gradep <= "4.0" and gradep > "3.7":
	print "You have an A!"