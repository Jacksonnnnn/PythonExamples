def beginning():
	print "Choose a number 1-5 to recieve your fortune..."
	next = raw_input("> ")
	if "1" in next:
		print "You will die in fire! haha"
		dead("How was being barbequed haha!")
	elif "2" in next:
		print "A bear will harm you with his claws..."
		dead("Thank you for feeding Tony :)")
	elif "3" in next:
		print "You will have good fortune..."
		good_fortune()
	elif "4" in next:
		print "Help Help!"
		man_sidewalk()
	elif "5" in next:
		print "You get into the college of your choosing!"
		college()
def college():
	print "Which college did you want to go to?"
	next = raw_input("> ")
	print "Ah you wanted to go to %s?" % next
	print "You get into the college you want, but then you overdose on pot and die at a party."
	dead("I guess you partied too hard...")
def good_fortune():
	print "You get many millions of dollars from the lottery!"
	print "Then after 2 months you get sued for all of your money by your employer. See? Working never did anyone any good..."
def man_sidewalk():
	print "A man walks on the side walk and suddenly falls. What do you do? Help them up, call an ambulance, or walk away?"
	next = raw_input("> ")
	if "help" in next:
		print "His heart exploded because of you picking him up too fast and too hard and you die due to the grief."
		dead("You're okay... there there...")
	elif "ambulance" in next:
		print "He dies before the ambulance gets there. You die due to grief."
		dead("You're okay... there there...")
	elif "walk away" in next:
		print "Good man. Walking away because that's not you're problem! The girl next to him turns out to be a nurse and he's alive still!"
def dead(why):
	print why, "Good job!"
	exit(0)
def start():
	beginning()
	
start()
