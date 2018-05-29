from math import pi
r = int(raw_input("What is the radius for your cylinder?  "))
h = int(raw_input("What is the height of your cylinder?  "))

a = pi * r ** 2
v = a * h

print "A cylinder with the radius of %s and the height of %s will have the volume of %s." % (r, h, v)