from math import log10

a = int(raw_input("What does 'a' equal?  "))
b = int(raw_input("What does 'b' equal?  "))

print a, "+", b, "equals", a + b
print a, "-", b, "equals", a - b
print a, "*", b, "equals", a * b
print a, "/", b, "equals", a / b
print a, "%", b, "equals", a % b

log = log10(a)
print "The base 10 logarithm of %s is %s" % (a, log)
exponant = a**b
print "%s^%s is %s" % (a, b, exponant)