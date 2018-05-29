mass = int(raw_input("In mililiters, what is the mass of your water?  "))
tempchange = int(raw_input("In celcius, what is the change in temperature of the water?  "))

water_heat_capacity = 4.186
electricity_price = 8.9
j_to_kwh =2.777e-7

q = mass * tempchange * water_heat_capacity

kwh = q * j_to_kwh
cost = kwh * electricity_price

print "That will be %s Joules of energy." % q
print "That will also be $%.2f dollars." % cost