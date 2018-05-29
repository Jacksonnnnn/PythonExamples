from math import sqrt
d = float(raw_input("What is the height from which the ball will be dropped?  "))
gravity = 9.8
 
vf = sqrt(2 * gravity * d)
 
print "It will hit the ground at %.2s m/s^2" % vf