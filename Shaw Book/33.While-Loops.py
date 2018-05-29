i = 0
max = 6
incriment = 1
numbers = []

while i < max:
	print "At the top i is %d" % i
	numbers.append(i)
	i = i + incriment
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	

print "The numbers: "

for num in numbers:
	print num