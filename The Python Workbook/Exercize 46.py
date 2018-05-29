month = raw_input("Enter the name of the month:  ")
day = int(raw_input("Enter the day number:  "))

if month == "January" or month == "February":
	season = "winter"
elif month == "March":
	if day < 20:
		season = "winter"
	else:
		season = "Spring"
elif month == "April" or month == "May":
	season = "spring"
elif month == "June":
	if day < 21:
		season = "spring"
	else:
		season = "summer"
elif month == "July" or month == "August":
	season = "summer"
elif month == "September":
	if day < 22:
		season = "summer"
	else:
		season = "fall"
elif month == "October" or month == "November":
	season = "fall"
elif month == "December":
	if day < 21:
		season = "fall"
	else:
		season = "winter"
print "%s %s is in the %s season." % (month, day, season)