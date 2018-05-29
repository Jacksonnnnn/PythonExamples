mag = float(raw_input("Please enter the Magnitude and I will tell you the Descriptor:  "))
if mag < 2.0:
	descriptor = "Micro"
elif mag >= 2.0 and mag <= 3.0:
	descriptor = "Very Minor"
elif mag >= 3.0 and mag <= 4.0:
	descriptor = "Minor"
elif mag >= 4.0 and mag <= 5.0:
	descriptor = "Light"
elif mag >= 5.0 and mag <= 6.0:
	descriptor = "Moderate"
elif mag >= 6.0 and mag <= 7.0:
	descriptor = "Strong"
elif mag >= 7.0 and mag <= 8.0:
	descriptor = "Major"
elif mag >= 8.0 and mag <= 10.0:
	descriptor = "Great"
elif mag >= 10.0:
	descriptor = "Meteoric"
	
print "The descriptor of your magnitude, %s, is %s." % (mag, descriptor)