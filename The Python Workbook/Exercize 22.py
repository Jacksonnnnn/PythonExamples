from math import sqrt

s1 = raw_input("What is the length of side 1?  ")
s2 = raw_input("What is the length of side 2?  ")
s3 = raw_input("What is the length of side 3?  ")

s = (s1 + s2 + s3 )/2
area = sqrt(s * (s - s1) * (s - s2) * (s - s3))

print "The area of a triangle with the side lengths of %s, %s, and %s has an area of %s units^2." % (s1, s2, s3, area)