date = raw_input("Please enter a date following the format provided (Ex. July 1):  ")

if date == "January 1" or date == "january 1":
	print "Your entered month and day corresponds to New Year's Day."
elif date == "July 1" or date == "july 1":
	print "Your entered month and day corresponds to Canada Day."
elif date == "December 25" or date == "december 25":
	print "Your entered month and day corresponds to Christmas Day."
else:
	print "Your entered month and day does not correspond to a fixed-date holiday."