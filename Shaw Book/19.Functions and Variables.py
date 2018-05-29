#This is defining a function: cheese and crackers that has two arguments being created in it.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
#Here they set the arguments with the function
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#Don't have to use the functions to get to the arguments. You can use variables instead of numbers aswell.
print "OR, we can use variables from out script:"
amount_of_cheese = 10
amount_of_crackers = 50

#Run the cheese and crackers function with variable arguments.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#You can use math to figure out what each argument is.
print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

#And that is seen here when you combine everything we've  done so far.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)


def presents_and_cake(presents, cake):
	print "You have %d presents!" % presents
	print "You have %d peices of cake!" % cake
	print "Man is it your Birthday or something?!"
	print "Go get the banners!\n"
	
print "Let's do the direct way of getting numbers:"
presents_and_cake(13, 17)

print "How about variables?"
number_of_presents = 16
peices_of_cake = 21

presents_and_cake(number_of_presents, peices_of_cake)

print "Hmmmmm how interesting..."
print "Let's see if you can do basic 1st grade math."
presents_and_cake(2+5, 3-1)

print "Variables and math?"
presents_and_cake(number_of_presents+14, peices_of_cake-3)