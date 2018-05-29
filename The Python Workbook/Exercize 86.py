def ordinal(o):
	if o == 1:
		print "first"
	if o == 2:
		print "second"
	if o == 3:
		print "third"
	if o == 4:
		print "fourth"
	if o == 5:
		print "fifth"
	if o == 6:
		print "sixth"
	if o == 7:
		print "seventh"
	if o == 8:
		print "eighth"
	if o == 9:
		print "ninth"
	if o == 10:
		print "tenth"
	if o == 11:
		print "eleventh"
	if o == 12:
		print "twelfth"
def displayVerse(n):
	print "On the", ordinal(n), "day of Christmas"
	print "my true love gave to me:"
	
	if n >= 12:
		print "Twelve drummers drumming,"
	if n >= 11:
		print "Eleven pipers piping,"
	if n >= 10:
		print "Ten lord a leaping,"
	if n >= 9:
		print "Nine ladies dancing,"
	if n >= 8:
		print "Eight maids a milking,"
	if n >= 7:
		print "Seven swans a swimming,"
	if n >= 6:
		print "Six geese a laying,"
	if n >= 5:
		print "Five golden rings,"
	if n >= 4:
		print "Four calling birds,"
	if n >= 3:
		print "Three French hens,"
	if n >= 2:
		print "Two turtle doves"
	if n == 1:
		print "A "
	else:
		print "And a "
		print "partridge in a pear tree."
def main():
	for verse in range(1, 13):
		displayVerse(verse)
main()