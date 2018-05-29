import pi from math
radius = int(raw_input("What is the radius of your circle/sphere?  "))

circle = pi * radius**2
sphere = 4/3 * pi * radius**3

print "A circle with a radius of %s has an area of %s." % (radius, circle)
print "A sphere with a radius of %s has a volume of %s." % (radius, sphere)