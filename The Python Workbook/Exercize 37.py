#User inputs the number of sides for the shape.
sides = raw_input("How many sides does your shape have?")

#Takes the input, and if it is one of the things listed, it prints the sentence under the if-statement.
if sides == "3":
	print "Your shape has 3 sides, which is a Triangle!"
elif sides == "4":
	print "Your shape has 4 sides, which is a Quadrilateral."
elif sides == "5":
	print "Your shape has 5 sides, which is a Pentagon."
elif sides == "6":
	print "Your shape has 6 sides, which is a Hexagon."
elif sides == "7":
	print "Your shape has 7 sides, which is a Septagon."
elif sides == "8":
	print "Your shape has 8 sides, which is a Octogon."
elif sides == "9":
	print "Your shape has 9 sides, which is a Nonagon."
elif sides == "10":
	print "Your shape has 10 sides, which is a Decagon."
else:
	print "Your shape has more or less sides than the range of 3 - 10 sides. Please try one of those sides."