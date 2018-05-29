month = raw_input("Enter the name of a month!  ")

days = 31

if month == "April" or month == "June" or month == "September" or month == "November":
	days = 30
elif month == "February":
	days = "28 or 29"

print month, "has", days, "days in it."