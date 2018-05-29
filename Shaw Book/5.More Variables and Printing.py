name = 'Zed A. Shaw'
age = 35 #that's not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually, that's not too heavy."
#If more than two variables that you're calling to %(letter), then do " % (var1, var2)". This can go on with multiple
#variable look at the last example
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#This is a very long and tricky line, stay with me.
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
