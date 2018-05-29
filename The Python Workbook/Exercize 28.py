airtemp = int(raw_input("What is the air temperature in Celsius?  "))
windspeed = int(raw_input("What is the windspeed in km/h?  "))

WCI = 13.12 + (0.6215 * airtemp) - (11.37 * (windspeed ** 0.16)) + (0.3965 * (airtemp * (windspeed ** 0.16)))

print "The Wind Chill Index is %s." % WCI