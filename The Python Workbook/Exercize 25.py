secondsraw = int(raw_input("What is the total number of seconds to convert into DHMS format?  "))
seconds = secondsraw
SPD = 86400
SPH = 3600
SPM = 60

days = seconds / SPD
seconds = seconds % SPD

hours = seconds / SPH
seconds = seconds % SPH

minutes = seconds / SPM
seconds = seconds % SPM

print "The equivilent to %s seconds in DHMS format is %d:%02d:%02d:%02d." % (seconds, days, hours, minutes, seconds)