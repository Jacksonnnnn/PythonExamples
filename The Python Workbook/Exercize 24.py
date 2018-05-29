days = raW_input("Number of Days?  ")
hours = raW_input("Number of Hours?  ")
minutes = raW_input("Number of Minutes?  ")
seconds = raW_input("Number of Seconds?  ")

rawdays = days * 24 * 60 * 60
rawhours = hours * 60 * 60
rawminutes = minutes * 60
rawseconds = seconds

totalseconds = rawdays + rawhours + rawminutes + rawseconds

print "%sd %sh %sm %ss converts to %s seconds." % (days, hours, minutes, seconds, totalseconds)