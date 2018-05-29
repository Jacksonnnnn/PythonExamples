#Defines the variables
people = 30
cars = 40
buses = 15

#If there are more cars than people, it runs...
if cars > people:
	#... this statement.
	print "We should take the cars."
	
#If there are more people than cars...	
elif cars < people:
	print "We should not take the cars."

#otherwise say "we can't decide"	
else:
	print "We can't decide."

#If there are more buses than cars...	
if buses > cars:
	print "That's too many buses."
	
#If there are more cars than buses...
elif buses < cars:
	print "Maybe we could take the buses."
	
#Everything else
else:
	print "We still can't decide."
	
#If there are more people than buses...
if people > buses:
	print "Alright, let's just take the buses."
	
#If it's too complicated then the'll just stay home.
else:
	print "Fine. Let's stay home then."