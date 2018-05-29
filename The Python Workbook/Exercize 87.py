WIDTH = 80

def center(s, width):
	if width < len(s):
		return s
	spaces = (width - len(s)) // 2
	result = " " * spaces + s
	
	return result

def main():
	print center("A Famous Story", WIDTH)
	print center("By:", WIDTH)
	print center("Someone Famous", WIDTH)
	print ""
	print "\tOnce upon a time so and so did so and so with so and so, so yeah..."
	print " and then some type of ending with a happy twist here please."
	
main()