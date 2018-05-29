pressure = int(raw_input("What is the pressure of your substance in kilopascals?  "))

PPSI = pressure / 6.89476
mercury = pressure / 0.133322
atmosphere = pressure / 101.325

print "%s Kilopascals is equivilent to %s pounds per square inch, %s millimeters of mercury, and %s atmospheres." % (pressure, PPSI, mercury, atmosphere)