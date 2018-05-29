month = raw_input("Enter the month you were born:  ")
day = int(raw_input("Enter the day you were born:    "))

if month == "January":
	if day <= 19:
		print "Capricorn."
	else:
		print "Aquarius."
elif month == "February":
	if day <= 18:
		print "Aquarius."
	else:
		print "Pisces."
elif month == "March":
	if day <= 20:
		print "Pisces."
	else:
		print "Aries."
elif month == "April":
	if day <= 19:
		print "Aries."
	else:
		print "Taurus."
elif month == "May":
	if day <= 20:
		print "Taurus."
	else:
		print "Gemini."
elif month == "June":
	if day <= 20:
		print "Gemini."
	else:
		print "Cancer."
elif month == "July":
	if day <= 22:
		print "Cancer."
	else:
		print "Leo."
elif month == "August":
	if day <= 22:
		print "Leo."
	else:
		print "Virgo."
elif month == "September":
	if day <= 22:
		print "Virgo."
	else:
		print "Libra."
elif month == "October":
	if day <= 22:
		print "Libra."
	else:
		print "Scorpio."
elif month == "November":
	if day <= 21:
		print "Scorpio."
	else:
		print "Sagittarius."
elif month == "December":
	if day <= 21:
		print "Sagittarius."
	else:
		print "Capricorn."