#Learning how to use %s within code and says there are 10 types of people.
x = "There are %d types of people." % 10
#variable for the words
binary = "binary"
do_not = "don't"
#There are those who know binary and those who don't.
y = "Those who know %s and those who %s." % (binary, do_not)

#prints the statements for x
print x
#then y
print y

#references the statments saying "I said this" and "I also said this".
print "I said: %r." % x
print "I also said: '%s'." % y

#Sets a variable to false (boolean)
hilarious = False
#Writes text with a reference variable at the end of it
joke_evaluation = "Isn't that joke so funny?! %r"

#Says that the joke is not funny.
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#After the ... it basically shows how it's now the right side (e)
print w + e