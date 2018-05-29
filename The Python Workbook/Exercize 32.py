a = int(raw_input("First number?  "))
b = int(raw_input("Second Number?  "))
c = int(raw_input("Third Number?  "))

min = min(a,b,c)
max = max(a,b,c)
middle = a + b + c - min - max

print "The numbers from highest to lowest are %s, %s, and %s." % (min, middle, max)