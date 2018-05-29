feet = int(raw_input("How many feet?  "))
inches = int(raw_input("How many inches?  "))

feetconv = (feet * 12) * 2.54
inchesconv = (inches * 2.54)
centimeters = (feetconv + inchesconv)

print "%s Ft. %s in. is %s cm." % (feet, inches, centimeters)