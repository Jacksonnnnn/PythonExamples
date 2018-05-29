length = float(raw_input("What is the length of your field in feet?  "))
width = float(raw_input("What is the width of your field in feet?  "))

area = length * width
conversion = area / 43560.0

print "Your field is %s acres." % conversion