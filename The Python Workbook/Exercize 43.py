note = float(raw_input("Enter the dollar amount that is on your bank note (#.## format):  "))

GW = 1.00
TJ = 2.00
AL = 5.00
AH = 10.00
AJ = 20.00
USG = 50.00
BF = 100.00

if note == GW:
	print "Your note has the face of George Washington ($1.00 bill)!"
elif note == TJ:
	print "Your note has the face of Thomas Jefferson ($2.00 bill)!"
elif note == AL:
	print "Your note has the face of Abraham Lincoln ($5.00 bill)!"
elif note == AH:
	print "Your note has the face of Alexander Hamilton ($10.00 bill)!"
elif note == AJ:
	print "Your note has the face of Andrew Jackson ($20.00 bill)!"
elif note == USG:
	print "Your note has the face of Ulysses S. Grant ($50.00 bill)!"
elif note == BF:
	print "Your note has the face of Benjamin Franklin ($100.00 bill)!"
else:
	print "Your note doesn't equal the amount of a face on a dollar bill. Please enter a dollar bill amount."