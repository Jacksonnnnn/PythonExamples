wavelength = raw_input("Enter a Wavelength in nm to see what color it is:  ")

if wavelength >= "380" and wavelength < "450":
	print "You have Violet light."
elif wavelength >= "450" and wavelength < "495":
	print "You have Blue light."
elif wavelength >= "495" and wavelength < "570":
	print "You have Green light."
elif wavelength >= "570" and wavelength < "590":
	print "You have Yellow light."
elif wavelength >= "590" and wavelength < "620":
	print "You have Orange light."
elif wavelength >= "620" and wavelength < "750":
	print "You have Red light."
elif wavelength > "750":
	print "Woah woah woah there, you're getting into Micro and Infared Radiation."
elif wavelength < "380":
	print "Woah woah woah there, you're getting into UV and Gamma Radiation."