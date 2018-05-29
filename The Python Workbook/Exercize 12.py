from math import *

xone = float(raw_input("What is the 'x' coordinate of your latitude?  "))
gone = float(raw_input("What is the 'y' coordinate of your latitude?  "))
xtwo = float(raw_input("What is the 'x' coordinate of your longitude?  "))
gtwo = float(raw_input("What is the 'y' coordinate of your longitude?  "))

distance = 6371 * acos(sin(xone)) * sin(xtwo) + cos(xone) * cos(xtwo) * cos(gone - gtwo)

print "The distance between your two points: (%s, %s) and (%s, %s) is %s" % (xone, gone, xtwo, gtwo, distance)