widgets = int(raw_input("How many widgets are you buying?  "))
gizmos = int(raw_input("How many gizmos are you buying?  "))

wweight = widgets * 75
gweight = gizmos * 112

totalweight = wweight + gweight
totalitems = widgets + gizmos

print "Your %s items will weigh %s grams." % (totalitems, totalweight)