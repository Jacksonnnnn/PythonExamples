measure = int(raw_input("What is your measurement in feet? I will convert it into inches, yards, and miles.  "))

inches = measure * 12
yards = measure / 3
miles = measure / 5280

print "%s ft is %s in, %s yd, and %s mi." % (measure, inches, yards, miles)