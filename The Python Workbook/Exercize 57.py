year = int(raw_input("Enter a year...  "))

if year % 400 == 0:
	isLeapYear = True
elif year % 100 == 0:
	isLeapYear = False
elif year % 4 == 0:
	isLeapYear = True
else:
	isLeapYear = False
	
if isLeapYear:
	print "%s is a leap year." % year
else:
	print "%s is not a leap year." % year