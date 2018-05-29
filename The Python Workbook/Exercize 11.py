# MPG -> L/100km
# Read value from user input and puts equivilent into L/100km

mpg = int(raw_input("How many Miles Per Gallon (MPG) are you trying to convert?  ")) 

lpkm = mpg / 235.21

print "You have %s L/100km from %s MPG" % (lpkm, mpg)